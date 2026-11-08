# 进销存三端界面风格候选

为微信小程序、手机 H5 和电脑网页准备的界面参考库。

**当前保存 A / B / C 三组候选，尚未选定默认风格，也不是三套可直接运行的程序。**
先保留真实界面、来源及研究说明，选定后再制作可复用模板。

## 候选对比

| 候选 | 视觉方向 | 适合参考的部分 | 详细页面 |
| --- | --- | --- | --- |
| A | 传统、紧凑的单据表格 | 电脑查询、批量操作、数量金额对比 | [查看 A](docs/candidates/a-compact.md) |
| B | 白底、少量强调色 | 筛选区、单据详情、样式变量组织 | [查看 B](docs/candidates/b-white.md) |
| C | 灰白、克制 | 浅线、文字层次、低干扰的库存页面 | [查看 C](docs/candidates/c-neutral.md) |

可以组合参考，例如 B 的信息结构与 C 的配色；电脑和手机不必照搬同一个布局。
选型不改变分批收货、审核及对账规则。

### A：传统紧凑型

来源：管伊佳 ERP（jshERP）。下图是原项目的采购入库界面，不是本仓库完成的新页面。
蓝色顶栏只作对照，不代表模板一定使用蓝白配色。

![A：采购入库原图](https://raw.githubusercontent.com/jishenghua/jshERP/8f5dc0877ffb4cf863f6cdd675ecac8fc1ce4ea1/jshERP-web/public/static/screenshot/3.jpg)

### B：白底与少量强调色

来源：仓图（warehouse）。重点参考筛选、表格和详情层次，不采用其完整菜单和手机彩色图标工作台。

![B：进货订单原图](https://raw.githubusercontent.com/sunjulei/warehouse/ed5f9a20459ecc79b56d72480bea321fff0d746f/img/%E8%BF%9B%E8%B4%A7%E7%AE%A1%E7%90%86-%E8%BF%9B%E8%B4%A7%E8%AE%A2%E5%8D%95.png)

### C：灰白简洁型

来源：ERPNext。重点参考文字、对齐和浅色分隔线；不引入完整 ERP 业务。
此图由固定版本 README 链接至官网，官网图片本身不是 Git 固定版本，可能变化。

![C：库存汇总原图](https://erpnext.com/files/v16_stock_summary.png)

## 三端与业务边界

- 电脑网页：可用紧凑表格，方便筛选、核对和批量查看。
- 小程序与 H5：使用纵向单据及分组表单，不直接缩小桌面表格。
- 配色、字号层次、状态含义可以统一；具体触控和安全区适配需实际验证。
- 功能范围是采购开单、审核、分批实际收货、材料库存、领料出库、预警和供应商对账。
- 不因参考图片出现零售、会员、会计、多仓等模块就增加需求。

## 来源与复用说明

截图通过原项目链接引用，没有将第三方图片、源码或完整系统重新打包进本仓库。
图片及原项目的权利归各自权利人；**视觉候选不等于代码授权或可运行模板**。
尤其 B 的许可包含额外销售限制，不能只按其标题当作标准 MIT。

详见 [来源、版本与使用边界](docs/sources.md)。

## 本地研究工具

需要 Python 3.10+；收集资料另需已安装的 GitHub CLI。
不需要安装或运行参考项目，也不需要 `uv`。

```text
python scripts/research.py collect
python scripts/research.py verify
python scripts/check_candidates.py
```

支持 shell 的环境也可使用相应入口：

```sh
sh scripts/research.sh collect
sh scripts/research.sh verify
sh scripts/check_candidates.sh
```

资料只保存到被 Git 忽略的 `.research-cache/`，日志写入 `logs/`。
本地研究与网络资料检查不是小程序真机、业务流程或部署验收。
