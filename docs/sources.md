# 来源、版本与使用边界

核对日期：2026-11-08。当前仓库保留三组候选参考，用户最新选定 B 为主视觉方向，不是三套已完成的程序。

## 来源版本

| 候选 | 项目 | 所查提交 | 许可文件观察 |
| --- | --- | --- | --- |
| A | [jishenghua/jshERP](https://github.com/jishenghua/jshERP) | `8f5dc0877ffb4cf863f6cdd675ecac8fc1ce4ea1` | [Apache 2.0](https://github.com/jishenghua/jshERP/blob/8f5dc0877ffb4cf863f6cdd675ecac8fc1ce4ea1/LICENSE) |
| B | [sunjulei/warehouse](https://github.com/sunjulei/warehouse) | `ed5f9a20459ecc79b56d72480bea321fff0d746f` | [正文含额外销售限制](https://github.com/sunjulei/warehouse/blob/ed5f9a20459ecc79b56d72480bea321fff0d746f/LICENSE)，不按标准 MIT 处理 |
| C | [frappe/erpnext](https://github.com/frappe/erpnext) | `b120a2e81ef017937df2e42912c18404ebadfb3d` | [GPL v3](https://github.com/frappe/erpnext/blob/b120a2e81ef017937df2e42912c18404ebadfb3d/license.txt) |

版本用于追踪研究来源，不承诺这是任何项目的最新发布版。
这些许可名称只是原文件的观察，不构成对第三方素材或具体使用方式的授权判断。

## 图片

- A 的三张图来自该提交的 `jshERP-web/public/static/screenshot/3.jpg`、`5.jpg`、`6.jpg`。
- B 的三张图来自该提交 README 所列的进货订单、订单详情、移动端工作台图片。
- C 的财务图来自固定提交；库存图来自 README 指向的官网地址，不是 Git 固定文件。
- 本仓库 Markdown 直接引用原图 URL，没有把第三方图片文件重新提交到仓库。
- 原图仅用于辨认候选风格，不冒充本仓库实现或本项目运行结果。
- 原链接若失效或内容变化，不能将这种变化解释为我们的模板变动；应重新核对来源。

## 源码观察范围

已读 A 的采购列表及部分样式、B 的样式变量/组件覆盖与手机进货订单；后续扩展到 ERPNext 采购状态、Aureus 紧凑主题与采购表单、Twenty 搜索/表格、Dolibarr 库存流水、Monica 分组表单。
七套固定源码已实际检出；具体文件、可参考做法与不采用项见 [源码级 UI/UX 分析](ui-ux-source-study.md)。
没有完成七个系统的全面代码审查，没有运行它们，也没有验证它们的全部采购和对账行为。

## 未包含

- 候选文档中不粘贴原项目整套代码、品牌素材或演示程序。另行通过 `references/` 子模块保存原仓库固定源码及原许可，不冒充自主实现。
- 没有安装参考项目依赖，未取得 Git LFS 指针指向的大文件对象。
- 本机研究缓存、日志、绝对路径、内部讨论和原业务项目资料。
- 真实客户、供应商、订单、手机号、生产配置、登录凭证或服务器密码。

以后实现模板时，仍需分别核对代码、图标、字体与素材来源。
候选阶段不为未核验的第三方内容统一加一个新许可证，也不自动宣称可直接商业分发。

## 验证方式

本仓库 `scripts/check_candidates.py` 检查候选文档、站内链接及全部外链图片响应，结果输出到 `logs/`。
本地收集脚本还可记录采集图片 SHA256；网络图册检查不能替代三端运行、业务流程和微信真机测试。
