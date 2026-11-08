"""核对参考源码实际检出、固定提交和未修改状态，不运行参考程序。"""

from dataclasses import asdict, dataclass
import json
import logging
import subprocess

from fetch_references import NAMES, ROOT


@dataclass(frozen=True)
class ReferenceState:
    name: str
    commit: str
    tracked_files: int
    missing_files: int
    clean: bool


def main() -> None:
    logs = ROOT / "logs"
    logs.mkdir(exist_ok=True)
    logging.basicConfig(level=logging.INFO, format="%(asctime)s %(message)s", handlers=[
        logging.StreamHandler(), logging.FileHandler(logs / "verify-references.log", encoding="utf-8")])
    states: list[ReferenceState] = []
    git = ["git", "-c", "core.longpaths=true"]
    for name in NAMES:
        relative = f"references/{name}"
        directory = ROOT / relative
        if not (directory / ".git").is_file():
            raise RuntimeError(f"参考源码尚未检出：{relative}")
        expected = subprocess.check_output(git + ["rev-parse", f":{relative}"],
                                            cwd=ROOT, encoding="ascii").strip()
        actual = subprocess.check_output(git + ["rev-parse", "HEAD"],
                                          cwd=directory, encoding="ascii").strip()
        if actual != expected:
            raise RuntimeError(f"源码版本与主仓库记录不一致：{relative}")
        tracked = subprocess.check_output(git + ["ls-files", "-z"], cwd=directory).count(b"\0")
        missing = subprocess.check_output(git + ["ls-files", "--deleted", "-z"],
                                          cwd=directory).count(b"\0")
        status = subprocess.check_output(git + ["status", "--porcelain", "--untracked-files=no"],
                                         cwd=directory)
        state = ReferenceState(name, actual, tracked, missing, not status.strip())
        if not state.clean or state.missing_files or not state.tracked_files:
            raise RuntimeError(f"源码缺失或已被修改：{relative}")
        states.append(state)
        logging.info("%s：%s 个文件，固定提交正确，工作区未修改", relative, tracked)
    (logs / "source-verification.json").write_text(
        json.dumps([asdict(state) for state in states], indent=2, ensure_ascii=False), encoding="utf-8")
    logging.info("七套源码核对通过，共 %s 个跟踪文件；未运行其业务或依赖脚本。",
                 sum(state.tracked_files for state in states))


if __name__ == "__main__":
    main()
