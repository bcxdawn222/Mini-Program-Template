"""收集界面研究资料，不安装或执行参考仓库的代码。"""

from __future__ import annotations

import argparse
import hashlib
import html
import json
import logging
import subprocess
import urllib.parse
import urllib.request
from dataclasses import asdict, dataclass
from html.parser import HTMLParser
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]


@dataclass(frozen=True)
class Repository:
    slug: str
    name: str


@dataclass(frozen=True)
class Screenshot:
    repo: str
    path: str
    filename: str
    title: str
    external_url: str = ""


@dataclass(frozen=True)
class Evidence:
    repository: str
    commit: str
    source_url: str
    filename: str
    title: str
    sha256: str
    size: int


@dataclass(frozen=True)
class Source:
    repo: str
    path: str
    filename: str


REPOSITORIES = (
    Repository("jishenghua/jshERP", "jshERP"),
    Repository("sunjulei/warehouse", "warehouse"),
    Repository("frappe/erpnext", "erpnext"),
)
SCREENSHOTS = (
    Screenshot("jshERP", "jshERP-web/public/static/screenshot/3.jpg",
               "a-purchase.jpg", "管伊佳：采购管理"),
    Screenshot("jshERP", "jshERP-web/public/static/screenshot/5.jpg",
               "a-stock.jpg", "管伊佳：仓库管理"),
    Screenshot("jshERP", "jshERP-web/public/static/screenshot/6.jpg",
               "a-finance.jpg", "管伊佳：财务管理"),
    Screenshot("warehouse", "img/进货管理-进货订单.png",
               "b-purchase.png", "仓图：进货订单"),
    Screenshot("warehouse", "img/订单详情.png",
               "b-detail.png", "仓图：订单详情"),
    Screenshot("warehouse", "img/移动端-工作台.png",
               "b-mobile.png", "仓图：移动端工作台"),
    Screenshot("erpnext", "erpnext/public/images/v16/hero_image.png",
               "c-workspace.png", "ERPNext：README 界面图"),
    Screenshot("erpnext", "", "c-stock.png", "ERPNext：库存汇总",
               "https://erpnext.com/files/v16_stock_summary.png"),
)
SOURCES = (
    Source("jshERP", "jshERP-web/src/views/bill/PurchaseInList.vue",
           "PurchaseInList.vue"),
    Source("jshERP", "jshERP-web/src/views/bill/modules/PurchaseInModal.vue",
           "PurchaseInModal.vue"),
    Source("jshERP", "jshERP-web/src/assets/less/common.less", "common.less"),
    Source("warehouse", "warehouse-front/src/styles/variables.scss",
           "variables.scss"),
    Source("warehouse", "warehouse-front/src/styles/element-overrides.scss",
           "element-overrides.scss"),
    Source("warehouse", "uniappx/pages/business/inport-order.uvue",
           "inport-order.uvue"),
)


def gallery(cache: Path, records: list[Evidence]) -> None:
    sections: list[str] = []
    for name, label in (
        ("jishenghua/jshERP", "A · 传统紧凑表格"),
        ("sunjulei/warehouse", "B · 白底、少量红色强调"),
        ("frappe/erpnext", "C · 灰白简洁"),
    ):
        images = []
        seen: set[str] = set()
        for record in records:
            if record.repository != name or record.sha256 in seen:
                continue
            seen.add(record.sha256)
            filename = html.escape(record.filename)
            title = html.escape(record.title)
            snapshot = f"引用仓库快照 {record.commit[:12]}"
            if not record.source_url.startswith("https://raw.githubusercontent.com/"):
                snapshot += "；图片为采集时官网文件，非 Git 固定版本"
            images.append(
                f'<figure><figcaption>{title}</figcaption>'
                f'<a href="{filename}" target="_blank">'
                f'<img src="{filename}" alt="{title}" loading="lazy"></a>'
                f'<p>来源：<a href="{html.escape(record.source_url)}">'
                f'原始图片</a> · {snapshot}</p></figure>'
            )
        sections.append(
            f'<section><h2>{label}</h2>{"".join(images)}</section>'
        )
    content = """<!doctype html>
<html lang="zh-CN"><meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>进销存界面风格对比</title>
<style>
*{box-sizing:border-box}body{margin:0;background:#fff;color:#262626;
font:16px/1.6 "Microsoft YaHei",sans-serif}main{max-width:1280px;
margin:auto;padding:24px}h1{font-size:24px}h2{font-size:20px}
section{padding:24px 0;border-top:1px solid #ddd}
figure{margin:24px 0 40px}figcaption{font-weight:600;margin-bottom:12px}
img{display:block;max-width:100%;height:auto;border:1px solid #ddd}
img[src="b-mobile.png"]{max-width:380px;width:100%}
a{color:#17683f}figure p{font-size:13px;color:#666}
</style><main><h1>进销存界面风格对比</h1>
<p>以下为项目公开的原始截图，不是已经完成的新系统。只选择视觉风格，不照搬功能。
手机和电脑可分别选择；分批收货、审核及实际收货对账流程保留。</p>
"""
    (cache / "index.html").write_text(
        content + "".join(sections) + "</main></html>\n", encoding="utf-8"
    )


def github_text(endpoint: str, query: str) -> str:
    result = subprocess.run(
        ["gh", "api", endpoint, "--jq", query],
        check=True, capture_output=True, encoding="utf-8",
    )
    return result.stdout.strip()


def download(url: str, target: Path) -> bytes:
    request = urllib.request.Request(
        url, headers={"User-Agent": "Mini-Program-Template-UI-Research"}
    )
    with urllib.request.urlopen(request, timeout=60) as response:
        data = response.read()
    target.write_bytes(data)
    return data


def collect() -> None:
    cache = ROOT / ".research-cache"
    cache.mkdir(exist_ok=True)
    commits: dict[str, str] = {}
    for repo in REPOSITORIES:
        sha = github_text(f"repos/{repo.slug}/commits/HEAD", ".sha")
        commits[repo.name] = sha
        folder = cache / repo.name
        folder.mkdir(exist_ok=True)
        download(
            f"https://raw.githubusercontent.com/{repo.slug}/{sha}/README.md",
            folder / "README.md",
        )
        license_path = github_text(f"repos/{repo.slug}/license", ".path")
        download(
            f"https://raw.githubusercontent.com/{repo.slug}/{sha}/"
            + urllib.parse.quote(license_path),
            folder / "LICENSE.txt",
        )
        logging.info("%s commit=%s", repo.slug, sha)

    for source in SOURCES:
        repo = next(item for item in REPOSITORIES if item.name == source.repo)
        download(
            f"https://raw.githubusercontent.com/{repo.slug}/{commits[repo.name]}/"
            + urllib.parse.quote(source.path),
            cache / repo.name / source.filename,
        )
        logging.info("已保存源码快照 %s/%s", repo.name, source.filename)

    records: list[Evidence] = []
    for shot in SCREENSHOTS:
        repo = next(item for item in REPOSITORIES if item.name == shot.repo)
        sha = commits[repo.name]
        url = shot.external_url or (
            f"https://raw.githubusercontent.com/{repo.slug}/{sha}/"
            + urllib.parse.quote(shot.path)
        )
        data = download(url, cache / shot.filename)
        if not (data.startswith(b"\x89PNG\r\n") or data.startswith(b"\xff\xd8")):
            raise ValueError(f"响应不是 PNG/JPEG 图片：{url}")
        records.append(Evidence(
            repo.slug, sha, url, shot.filename, shot.title,
            hashlib.sha256(data).hexdigest(), len(data),
        ))
        logging.info("已保存 %s (%d bytes)", shot.filename, len(data))
    (cache / "manifest.json").write_text(
        json.dumps([asdict(record) for record in records],
                   ensure_ascii=False, indent=2) + "\n",
        encoding="utf-8",
    )
    gallery(cache, records)
    logging.info("完成：%s", cache)


class GalleryParser(HTMLParser):
    def __init__(self) -> None:
        super().__init__()
        self.images: list[str] = []
        self.section_count = 0

    def handle_starttag(
        self, tag: str, attrs: list[tuple[str, str | None]]
    ) -> None:
        if tag == "section":
            self.section_count += 1
        if tag == "img":
            for key, value in attrs:
                if key == "src" and value:
                    self.images.append(value)


def verify() -> None:
    cache = ROOT / ".research-cache"
    records = [
        Evidence(**record)
        for record in json.loads((cache / "manifest.json").read_text("utf-8"))
    ]
    for record in records:
        data = (cache / record.filename).read_bytes()
        if len(data) != record.size:
            raise ValueError(f"文件大小不匹配：{record.filename}")
        if hashlib.sha256(data).hexdigest() != record.sha256:
            raise ValueError(f"文件校验不匹配：{record.filename}")
    parser = GalleryParser()
    parser.feed((cache / "index.html").read_text("utf-8"))
    expected = {record.filename for record in records}
    unique_images = {(record.repository, record.sha256) for record in records}
    if parser.section_count != 3 or len(parser.images) != len(unique_images):
        raise ValueError("图册分组或图片数量与来源清单不一致")
    for filename in parser.images:
        if filename not in expected or not (cache / filename).is_file():
            raise ValueError(f"图册图片链接无效：{filename}")
    logging.info("校验通过：三组、%d 张不同图片；原图哈希与链接有效",
                 len(unique_images))


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("command", choices=["collect", "verify"])
    arguments = parser.parse_args()
    logs = ROOT / "logs"
    logs.mkdir(exist_ok=True)
    logging.basicConfig(
        level=logging.INFO, format="%(asctime)s %(levelname)s %(message)s",
        handlers=[
            logging.FileHandler(logs / "research.log", encoding="utf-8"),
            logging.StreamHandler(),
        ],
    )
    try:
        if arguments.command == "collect":
            collect()
        else:
            verify()
    except Exception:
        logging.exception("研究资料收集失败")
        raise


if __name__ == "__main__":
    main()
