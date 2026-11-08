# ERP、CRM 与界面候选源码

记录日期：2026-11-08。五个 ERP/CRM 项目及 A、B 两个界面候选分别 fork 到 `bcxdawn222`，通过本仓库的 Git 子模块集中保存固定源码版本。
七套源码已实际检出到本地 `references/`，不是仅保存网址。各项目没有改装、运行或接入现有业务。

## 七个入口

| 项目 | 当前账号下的 fork | 原仓库 | 集中入口 |
| --- | --- | --- | --- |
| ERPNext | [bcxdawn222/erpnext](https://github.com/bcxdawn222/erpnext) | [frappe/erpnext](https://github.com/frappe/erpnext) | `references/erpnext` |
| Aureus ERP | [bcxdawn222/aureuserp](https://github.com/bcxdawn222/aureuserp) | [aureuserp/aureuserp](https://github.com/aureuserp/aureuserp) | `references/aureuserp` |
| Twenty | [bcxdawn222/twenty](https://github.com/bcxdawn222/twenty) | [twentyhq/twenty](https://github.com/twentyhq/twenty) | `references/twenty` |
| Dolibarr | [bcxdawn222/dolibarr](https://github.com/bcxdawn222/dolibarr) | [Dolibarr/dolibarr](https://github.com/Dolibarr/dolibarr) | `references/dolibarr` |
| Monica | [bcxdawn222/monica](https://github.com/bcxdawn222/monica) | [monicahq/monica](https://github.com/monicahq/monica) | `references/monica` |
| B 仓图 | [bcxdawn222/warehouse](https://github.com/bcxdawn222/warehouse) | [sunjulei/warehouse](https://github.com/sunjulei/warehouse) | `references/warehouse` |
| A 管伊佳 | [bcxdawn222/jshERP](https://github.com/bcxdawn222/jshERP) | [jishenghua/jshERP](https://github.com/jishenghua/jshERP) | `references/jshERP` |

Aureus ERP 和 Dolibarr 使用上表核对过的完整仓库名，不使用转发文字里截断的名称。
fork 保留各自的上游关系；本仓库不把不同项目的代码、历史或许可证合并。

## 本次固定版本

子模块指向下列提交，不会因上游更新而静默改变。

| 入口 | 分支 | 固定提交 |
| --- | --- | --- |
| `references/erpnext` | `develop` | `b120a2e81ef017937df2e42912c18404ebadfb3d` |
| `references/aureuserp` | `master` | `c31a0db21e00fa436c4949eb4f60ceef81e116ec` |
| `references/twenty` | `main` | `fbe38eec9a141ce305ded44819133f636c9041e1` |
| `references/dolibarr` | `develop` | `80eb087226f07475e4df1026b4cb048c7181e90e` |
| `references/monica` | `main` | `dab74273acc5c9e0ba713a9f7c2c71c24ab16993` |
| `references/warehouse` | `master` | `ed5f9a20459ecc79b56d72480bea321fff0d746f` |
| `references/jshERP` | `master` | `8f5dc0877ffb4cf863f6cdd675ecac8fc1ce4ea1` |

本次检出文件数依次为 5,955、11,628、42,872、15,610、2,093、507、718，共 79,383 个 Git 跟踪文件。
这表示固定版本源码到位，不表示全部文件已通读或各系统已运行验收。

## 查看与获取

在 GitHub 打开 `references/` 下的项目，可以进入对应 fork 的固定源码版本。
普通 GitHub ZIP 下载不会带入子模块源码。新电脑克隆本仓库后，使用 Python 与 Git 获取全部七套源码：

```text
python scripts/fetch_references.py
python scripts/verify_references.py
```

也可只取一个项目：

```text
python scripts/fetch_references.py --repo warehouse
```

支持 shell 的环境可使用 `scripts/fetch_references.sh` 与 `scripts/verify_references.sh`。
脚本按主仓库记录的提交检出；不自动更新到上游新版本，不安装依赖、启动服务或导入数据库。
为避免自动下载大体积媒体，Git LFS 文件保留其指针，不自动取得 LFS 对象；本次各项目根目录未发现额外的嵌套子模块清单。
验证脚本检查实际 HEAD、主仓库固定提交、缺失文件及未修改状态，结果保存在 `logs/`。
没有访问参考项目配置中的任何服务或账号。

## UI/UX 研读

详见 [源码级界面与交互分析](ui-ux-source-study.md)。以用户选定的 B 为视觉主方向，其他系统提供信息密度、状态动作、来源追溯等参考，不混成七种配色。

## 使用边界

各项目保留自己的许可文件及版权说明，根目录的候选文档不替它们重新授权。
fork 和集中存放不代表可以不受限制地复制、销售或移除署名；正式复用具体代码前，需单独检查对应版本的许可及第三方依赖。
本次不照搬转发文字中的 star 数、框架版本或功能宣传，也没有把它们当作已验证结论。
当前系统仍按已确认的采购、分批实收、库存出库及对账需求完善，不因为收藏五套系统就引入全部 ERP/CRM 功能。

[返回首页](../README.md) · [当前选择的 B 风格](style-direction.md)
