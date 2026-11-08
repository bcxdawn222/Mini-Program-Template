# ERP 与 CRM 源码收藏

记录日期：2026-11-08。按用户要求，五个项目分别 fork 到 `bcxdawn222`，再通过本仓库的 Git 子模块集中提供入口。
这是真实 fork，不是仅收藏上游网址；各项目没有改装、运行或接入现有业务。

## 五个入口

| 项目 | 当前账号下的 fork | 原仓库 | 集中入口 |
| --- | --- | --- | --- |
| ERPNext | [bcxdawn222/erpnext](https://github.com/bcxdawn222/erpnext) | [frappe/erpnext](https://github.com/frappe/erpnext) | `references/erpnext` |
| Aureus ERP | [bcxdawn222/aureuserp](https://github.com/bcxdawn222/aureuserp) | [aureuserp/aureuserp](https://github.com/aureuserp/aureuserp) | `references/aureuserp` |
| Twenty | [bcxdawn222/twenty](https://github.com/bcxdawn222/twenty) | [twentyhq/twenty](https://github.com/twentyhq/twenty) | `references/twenty` |
| Dolibarr | [bcxdawn222/dolibarr](https://github.com/bcxdawn222/dolibarr) | [Dolibarr/dolibarr](https://github.com/Dolibarr/dolibarr) | `references/dolibarr` |
| Monica | [bcxdawn222/monica](https://github.com/bcxdawn222/monica) | [monicahq/monica](https://github.com/monicahq/monica) | `references/monica` |

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

## 查看与获取

在 GitHub 打开 `references/` 下的项目，可以进入对应 fork 的固定源码版本。
普通 ZIP 下载不会带入子模块源码；需要离线源码时，单独下载对应 fork，或在克隆本仓库后执行：

```text
git submodule update --init --depth 1 references/erpnext
```

将末尾路径替换为上表其他入口即可按需下载。一次获取全部五个项目：

```text
git submodule update --init --depth 1
```

上述命令只获取源码，不安装依赖、启动服务或导入数据库。
本次没有克隆并运行这些项目，没有访问它们配置中的任何服务或账号。

## 使用边界

各项目保留自己的许可文件及版权说明，根目录的候选文档不替它们重新授权。
fork 和集中存放不代表可以不受限制地复制、销售或移除署名；正式复用具体代码前，需单独检查对应版本的许可及第三方依赖。
本次不照搬转发文字中的 star 数、框架版本或功能宣传，也没有把它们当作已验证结论。
当前系统仍按已确认的采购、分批实收、库存出库及对账需求完善，不因为收藏五套系统就引入全部 ERP/CRM 功能。

[返回首页](../README.md) · [当前选择的 B 风格](style-direction.md)
