"""检出固定版本的参考源码；不安装依赖、不启动参考项目。"""

import argparse
import logging
import os
from pathlib import Path
import subprocess


ROOT = Path(__file__).resolve().parents[1]
NAMES = ("erpnext", "aureuserp", "twenty", "dolibarr", "monica", "warehouse", "jshERP")


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--repo", choices=NAMES)
    args = parser.parse_args()
    logs = ROOT / "logs"
    logs.mkdir(exist_ok=True)
    logging.basicConfig(level=logging.INFO, format="%(asctime)s %(message)s", handlers=[
        logging.StreamHandler(), logging.FileHandler(logs / "fetch-references.log", encoding="utf-8")])
    environment = os.environ.copy()
    environment["GIT_TERMINAL_PROMPT"] = "0"
    environment["GIT_LFS_SKIP_SMUDGE"] = "1"
    for name in (args.repo,) if args.repo else NAMES:
        relative = f"references/{name}"
        logging.info("正在检出 %s", relative)
        command = ["git", "-c", "core.longpaths=true", "-c", "protocol.file.allow=never",
                   "submodule", "update", "--init", "--depth", "1", "--checkout", "--", relative]
        result = subprocess.run(command, cwd=ROOT, env=environment, stdout=subprocess.PIPE,
                                stderr=subprocess.STDOUT, encoding="utf-8", errors="replace")
        logging.info("%s", result.stdout.strip())
        if result.returncode:
            raise SystemExit(result.returncode)
        if os.name == "nt":
            subprocess.run(["git", "config", "core.longpaths", "true"], cwd=ROOT / relative, check=True)
        commit = subprocess.check_output(["git", "-C", str(ROOT / relative), "rev-parse", "HEAD"],
                                         cwd=ROOT, encoding="ascii").strip()
        files = subprocess.check_output(["git", "-C", str(ROOT / relative), "ls-files", "-z"],
                                        cwd=ROOT)
        logging.info("已检出 %s，提交 %s，跟踪文件 %s 个", relative, commit, files.count(b"\0"))
    logging.info("源码检出完成；未安装依赖或运行参考程序。")


if __name__ == "__main__":
    main()
