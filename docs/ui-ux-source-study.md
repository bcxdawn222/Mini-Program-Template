# 源码级 UI/UX 分析与仿照范围

研究日期：2026-11-08。用户已选择 B 候选作为主方向。本文基于实际检出的源文件，不以项目宣传或截图代替源码证据。
七套参考代码均未运行；本文不是整库审计、运行效果报告或许可意见。

## 这次仿照什么

不是把七套系统的颜色和组件混起来，也不是复制完整 ERP。
仿照的是正常业务软件的信息组织：常用查询在前、单据状态明确、金额数量对齐、来源可追查、操作紧邻对应记录。

| 位置 | 我们需要的组织方式 | 不采用 |
| --- | --- | --- |
| 电脑采购 | 紧凑筛选、单号/供应商/状态/采购人/日期、材料明细及合计 | 巨大欢迎区、彩色统计墙、几十项常驻筛选 |
| 手机采购 | 查询与状态在前，纵向单据显示来源和登记信息，详情展示逐批实收 | 电脑表格等比缩小、商城促销图、emoji 九宫格 |
| 材料库存 | 名称/型号/单位/余额/阈值，预警置前，领用和明细操作 | 未确认的多仓、零售价、会员和销售 POS |
| 供应商对账 | 供应商、月份、实收金额、未交数量、原采购单及确认记录 | 将采购下单金额直接当成本月已收应付 |
| 审核与收货 | 当前状态、可执行操作、成功/失败/空结果分别呈现 | 按钮只改变外观、失败后残留旧数据、员工自动发货 |

## B 仓图：主视觉来源

固定版本：`ed5f9a20459ecc79b56d72480bea321fff0d746f`。

- [样式变量](https://github.com/bcxdawn222/warehouse/blob/ed5f9a20459ecc79b56d72480bea321fff0d746f/warehouse-front/src/styles/variables.scss)：白色主体，`#e11d48` 强调色，11～24px 字号层级，4/8/12/16/20/24px 间距，4/6/8px 小圆角。颜色、字体、间距分组维护，而不是每页临时配色。
- [Element Plus 覆盖](https://github.com/bcxdawn222/warehouse/blob/ed5f9a20459ecc79b56d72480bea321fff0d746f/warehouse-front/src/styles/element-overrides.scss)：按钮、输入框等从变量取值，桌面普通按钮高 32px；这个高度不直接用于手机。
- [电脑进货单](https://github.com/bcxdawn222/warehouse/blob/ed5f9a20459ecc79b56d72480bea321fff0d746f/warehouse-front/src/views/business/inport-order/index.vue)：查询、表格、详情、打印分开；金额右对齐，备注溢出提示，操作列固定右侧，详情头先列单号、供应商和时间，再放材料行与合计。
- [手机进货单](https://github.com/bcxdawn222/warehouse/blob/ed5f9a20459ecc79b56d72480bea321fff0d746f/uniappx/pages/business/inport-order.uvue)：不是桌面表格缩放；使用订单号与状态的横向头部，金额/时间纵向排列，底部独立操作，详情在限高滚动层内显示。列表间距 16rpx、左右 24rpx，单据内边距 24rpx。

我们采用：白底、浅灰分隔、少量强调、清楚的单据主次、手机单独排版。
不采用：渐变主按钮、悬停上移、负字距、彩色 emoji、嵌套卡片、蓝色手机主按钮及整单退货逻辑。

其网页“加货/退货”和手机“整单退货”不是我们已确认的分批实收业务，不能因页面类似就复用算法。
原许可带额外销售限制；本次保留原仓库和许可，业务项目采用自主实现，没有复制其页面源码或素材。

## A 管伊佳：桌面筛选与信息密度

固定版本：`8f5dc0877ffb4cf863f6cdd675ecac8fc1ce4ea1`。

[采购入库列表](https://github.com/bcxdawn222/jshERP/blob/8f5dc0877ffb4cf863f6cdd675ecac8fc1ce4ea1/jshERP-web/src/views/bill/PurchaseInList.vue)：
常用单据编号、商品信息、日期在第一行；供应商等次要筛选由“展开/收起”控制。栅格区分桌面与窄屏，查询和重置并列。

我们采用：常用条件优先，次要条件不常驻占满首屏；桌面保持可扫描的表格。
不采用：整套 Ant Design Vue 旧工程、蓝色通栏、全部仓库/财务筛选和卡片包裹。
源码出现部分入库状态，不等于已验证完整业务，也不能认定它不支持分批。

## ERPNext：状态必须反映业务进度

固定版本：`b120a2e81ef017937df2e42912c18404ebadfb3d`。

- [采购列表状态](https://github.com/bcxdawn222/erpnext/blob/b120a2e81ef017937df2e42912c18404ebadfb3d/erpnext/buying/doctype/purchase_order/purchase_order_list.js)：按 `per_received`、`per_billed` 与单据状态区分待收货、待开票、完成；不同动作另外检查对应创建权限。
- [采购表单](https://github.com/bcxdawn222/erpnext/blob/b120a2e81ef017937df2e42912c18404ebadfb3d/erpnext/buying/doctype/purchase_order/purchase_order.js)：材料行按订购量与已收量设置指示；交货日期等表头信息可影响明细，但收货状态不是填一个固定标签。
- [关联单据定义](https://github.com/bcxdawn222/erpnext/blob/b120a2e81ef017937df2e42912c18404ebadfb3d/erpnext/buying/doctype/purchase_order/purchase_order_dashboard.py)：采购单与收货、发票、支付等来源分组关联，不把所有过程揉进一行。

我们采用：已收/未交数量与状态一致，收货记录能找到原采购单，审核后才显示后续动作。
不采用：完整财务、制造、分包菜单，或以“开票完成”替代我们的老板对账确认。
ERPNext 应用样式引用主题变量；完整 Frappe 基础框架不在这个子模块中，尚未据此拆出独立三端组件库。

## Aureus：紧凑度是统一规则

固定版本：`c31a0db21e00fa436c4949eb4f60ceef81e116ec`。

- [共享主题](https://github.com/bcxdawn222/aureuserp/blob/c31a0db21e00fa436c4949eb4f60ceef81e116ec/resources/css/filament/shared/theme.css)：白色顶栏和侧栏、细边框、取消顶栏阴影；正文、标题、说明分别定义字号，当前导航用窄边线和浅底表示。
- [紧凑覆盖](https://github.com/bcxdawn222/aureuserp/blob/c31a0db21e00fa436c4949eb4f60ceef81e116ec/resources/css/filament/shared/compact.css)：页面间距、表格单元格、工具栏、分页、弹窗一起收紧。不是只把标题改小。
- [采购表格定义](https://github.com/bcxdawn222/aureuserp/blob/c31a0db21e00fa436c4949eb4f60ceef81e116ec/plugins/webkul/purchases/src/Filament/Admin/Clusters/Orders/Resources/OrderResource/Tables/OrdersTable.php)：单号/供应商可搜索排序，金额使用货币格式，状态用文字标签；开票和收货状态列默认隐藏，降低第一眼的信息量。
- [采购表单定义](https://github.com/bcxdawn222/aureuserp/blob/c31a0db21e00fa436c4949eb4f60ceef81e116ec/plugins/webkul/purchases/src/Filament/Admin/Clusters/Orders/Resources/OrderResource/Schemas/OrderForm.php)：状态步骤只读，供应商可搜索，必填与状态禁用明确；表单分为通用信息及后续分组。

我们采用：统一间距与字号、默认少列、必要字段明显、只在正确状态提供操作。
不采用：采购协议、币种、全部企业权限配置，也不把 Filament/PHP 代码直接塞进现有 Vue/uni-app 项目。

## Twenty：组件细节与可用性

固定版本：`fbe38eec9a141ce305ded44819133f636c9041e1`。

- [间距定义](https://github.com/bcxdawn222/twenty/blob/fbe38eec9a141ce305ded44819133f636c9041e1/packages/twenty-ui/design-tokens/spacing.ts)：以 4px 为主步长，补 2/6px，主题生成文件统一消费，不在页面到处猜间距。
- [搜索输入结构](https://github.com/bcxdawn222/twenty/blob/fbe38eec9a141ce305ded44819133f636c9041e1/packages/twenty-ui/src/components/input/SearchInput/SearchInput.tsx)：输入组、搜索图标和后续操作分离，自动 id，并提供 `aria-label`/`aria-labelledby`。
- [搜索布局](https://github.com/bcxdawn222/twenty/blob/fbe38eec9a141ce305ded44819133f636c9041e1/packages/twenty-ui/src/components/input/SearchInput/SearchInput.module.scss)：输入组 `flex:1; min-width:0`，图标随焦点变化，不挤掉操作按钮。
- [表格行](https://github.com/bcxdawn222/twenty/blob/fbe38eec9a141ce305ded44819133f636c9041e1/packages/twenty-front/src/modules/ui/layout/table/components/TableRow.tsx)：选中、展开、悬停分开，移动端列轨道可单独设置；键盘事件和展开语义可传入。
- [单元格](https://github.com/bcxdawn222/twenty/blob/fbe38eec9a141ce305ded44819133f636c9041e1/packages/twenty-front/src/modules/ui/layout/table/components/TableCell.tsx)：高度、内边距、对齐和溢出明确配置；并非每个单元格都靠自由伸缩。

我们采用：搜索按钮不被长输入挤出；状态不被长单号遮挡；可点击和禁用状态明确；键盘及触控都能完成常用操作。
不采用：CRM 管道、整套 React 状态架构、其主题强调色或桌面低高度控件直接移到手机。

## Dolibarr：业务来源比装饰更重要

固定版本：`80eb087226f07475e4df1026b4cb048c7181e90e`。

- [供应商订单列表](https://github.com/bcxdawn222/dolibarr/blob/80eb087226f07475e4df1026b4cb048c7181e90e/htdocs/fourn/commande/list.php)：单号、供应商编号、状态和日期各自为筛选条件，读取、添加、审核权限分开。
- [库存流水](https://github.com/bcxdawn222/dolibarr/blob/80eb087226f07475e4df1026b4cb048c7181e90e/htdocs/product/stock/movement_list.php)：日期、产品、批次、来源、数量等列独立；作者、采购价值等字段并非全部默认显示。

我们采用：余额能追溯到具体来料/领用记录，显示日期、数量、单位与来源；库存端不因拥有出库密码就自动暴露采购价格。
不采用：旧式 PHP 页面布局照搬、复杂单据菜单、多币种和多仓业务。

## Monica：分组记录与手机控件

固定版本：`dab74273acc5c9e0ba713a9f7c2c71c24ab16993`。

- [备注分组](https://github.com/bcxdawn222/monica/blob/dab74273acc5c9e0ba713a9f7c2c71c24ab16993/resources/js/Shared/Modules/Notes.vue)：标题及新增操作靠在一起；记录正文与日期/作者分层，空闲状态不一直展示编辑表单，保存和取消集中在表单尾部。
- [文本输入](https://github.com/bcxdawn222/monica/blob/dab74273acc5c9e0ba713a9f7c2c71c24ab16993/resources/js/Shared/Form/TextInput.vue)：显式关联标签和输入 id，区分选填、禁用、帮助文字。
- [分页](https://github.com/bcxdawn222/monica/blob/dab74273acc5c9e0ba713a9f7c2c71c24ab16993/resources/js/Components/Pagination.vue)：手机显示前后页，桌面显示摘要及页码；同一数据来源采用不同布局。

我们采用：单据备注与操作记录分层、字段标签明确、手机与电脑分别组织控件。
不采用：个人关系、情绪和联系人功能，或将这套 CRM 作为采购库存业务基础。
代码中存在不适合直接照抄的分支与通用类型，当前仅记录观察，没有验证全部交互正确性。

## 应用到现有系统的顺序

1. 手机采购列表：紧凑页头、资料与对账入口、状态筛选、搜索、白底单据和底部导航；长单号保留完整换行。
2. 采购表单及详情：延续同一字体和间距，含税/不含税单列切换；材料、收货进度、批次记录、审核操作分组，不删业务字段。
3. 材料库存与明细：余额和阈值突出；预警状态与备货选择分离；领用表单的数量和时间易于触控。
4. 对账与电脑网页：保持供应商和月份身份明确、实收与未交分开；电脑使用紧凑表格而不是铺满手机卡片。

这是按页面实施的范围，不是宣称四步已全部完成。手机视觉认可、H5 行为检查、小程序编译、微信真机与上线分别记录。

## 检查要求

- 320/390/430px 手机宽度及桌面布局分别查看；长单号、长供应商名、空列表、失败、翻页重试都需检查。
- 主要手机操作保持约 44px 触控高度；不将桌面 28/32px 紧凑按钮直接搬过去。
- 配色检查包含图标文件和原生底部导航，不能只改 Vue 按钮。
- 参考项目源码只读；不安装、运行其依赖，不访问其配置中的服务。
- 不将截图、源码研读或编译通过写成“全部功能没有问题”。

[返回首页](../README.md) · [固定源码与获取方式](open-source-references.md) · [当前 B 风格规则](style-direction.md)
