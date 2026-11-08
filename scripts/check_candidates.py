"""核对公开候选资料及链接，不执行任何参考项目。"""

from __future__ import annotations

import logging
import re
import urllib.parse
import urllib.request
from html.parser import HTMLParser
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
DOCUMENTS = (
    ROOT / "README.md",
    ROOT / "docs" / "sources.md",
    ROOT / "docs" / "style-direction.md",
    ROOT / "docs" / "candidates" / "a-compact.md",
    ROOT / "docs" / "candidates" / "b-white.md",
    ROOT / "docs" / "candidates" / "c-neutral.md",
)


class Images(HTMLParser):
    def __init__(self) -> None:
        super().__init__()
        self.sources: set[str] = set()

    def handle_starttag(
        self, tag: str, attrs: list[tuple[str, str | None]]
    ) -> None:
        if tag == "img":
            for key, value in attrs:
                if key == "src" and value:
                    self.sources.add(value)


def check() -> None:
    image_urls: set[str] = set()
    source_urls: set[str] = set()
    for document in DOCUMENTS:
        text = document.read_text(encoding="utf-8")
        if re.search(r"(?<![A-Za-z])[A-Za-z]:[\\/]|\.research-cache[/\\].+\.vue", text):
            raise ValueError(f"公开文档含不应发布的本地内容：{document.name}")
        if re.search(r"""(?i)(password|api[_-]?key|token)\s*[:=]\s*['"][^'"]{6,}""", text):
            raise ValueError(f"公开文档含疑似硬编码凭证：{document.name}")
        if "候选" not in text:
            raise ValueError(f"未明确候选状态：{document.name}")
        parser = Images()
        parser.feed(text)
        image_urls.update(parser.sources)
        image_urls.update(re.findall(r"!\[[^\]]*\]\((https://[^)\s]+)\)", text))
        for target in re.findall(r"\[[^\]]*\]\(([^)\s]+)\)", text):
            parsed = urllib.parse.urlparse(target)
            if parsed.scheme:
                if parsed.scheme != "https":
                    raise ValueError(f"外链不是 HTTPS：{target}")
                source_urls.add(target)
                continue
            path = (document.parent / urllib.parse.unquote(parsed.path)).resolve()
            if not path.is_relative_to(ROOT) or not path.is_file():
                raise ValueError(f"站内链接无效：{document.name} → {target}")
        logging.info("文档及站内链接通过：%s", document.relative_to(ROOT))

    if len(image_urls) != 8:
        raise ValueError("候选应包含八个不同的图片来源链接")
    for url in sorted(image_urls):
        request = urllib.request.Request(
            url, headers={"User-Agent": "Mini-Program-Template-Candidate-Check"}
        )
        with urllib.request.urlopen(request, timeout=60) as response:
            signature = response.read(12)
            if not (
                signature.startswith(b"\x89PNG\r\n")
                or signature.startswith(b"\xff\xd8")
            ):
                raise ValueError(f"图片链接未返回 PNG/JPEG：{url}")
        logging.info("图片响应通过：%s", url)

    # 用原始文件接口检查固定版本的源码、说明和许可引用。
    for url in sorted(source_urls - image_urls):
        match = re.fullmatch(
            r"https://github.com/([^/]+/[^/]+)/blob/([a-f0-9]{40})/(.+)", url
        )
        if not match:
            continue
        slug, commit, path = match.groups()
        raw = f"https://raw.githubusercontent.com/{slug}/{commit}/{path}"
        with urllib.request.urlopen(raw, timeout=60) as response:
            if not response.read(1):
                raise ValueError(f"来源引用为空：{url}")
        logging.info("固定版本来源引用通过：%s", url)
    logging.info("完成：%d 份公开文档、三组候选、八个外链原图", len(DOCUMENTS))


def main() -> None:
    folder = ROOT / "logs"
    folder.mkdir(exist_ok=True)
    logging.basicConfig(
        level=logging.INFO,
        format="%(asctime)s %(levelname)s %(message)s",
        handlers=[
            logging.FileHandler(folder / "candidate-check.log", encoding="utf-8"),
            logging.StreamHandler(),
        ],
    )
    try:
        check()
    except Exception:
        logging.exception("候选资料检查失败")
        raise


if __name__ == "__main__":
    main()
