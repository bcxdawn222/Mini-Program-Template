# A：传统紧凑单据型

状态：候选，未选定，未实现为可运行模板。

## 真实界面

原项目：[管伊佳 ERP（jshERP）](https://github.com/jishenghua/jshERP/tree/8f5dc0877ffb4cf863f6cdd675ecac8fc1ce4ea1)。

### 采购入库

![采购入库](https://raw.githubusercontent.com/jishenghua/jshERP/8f5dc0877ffb4cf863f6cdd675ecac8fc1ce4ea1/jshERP-web/public/static/screenshot/3.jpg)

### 其它入库

![其它入库](https://raw.githubusercontent.com/jishenghua/jshERP/8f5dc0877ffb4cf863f6cdd675ecac8fc1ce4ea1/jshERP-web/public/static/screenshot/5.jpg)

### 财务收入单

此图仅用于比较财务表格的密度与排列，不是供应商月度对账页面。

![财务收入单](https://raw.githubusercontent.com/jishenghua/jshERP/8f5dc0877ffb4cf863f6cdd675ecac8fc1ce4ea1/jshERP-web/public/static/screenshot/6.jpg)

## 样式写法观察

已读取 [采购入库列表源码](https://github.com/jishenghua/jshERP/blob/8f5dc0877ffb4cf863f6cdd675ecac8fc1ce4ea1/jshERP-web/src/views/bill/PurchaseInList.vue)：

- 第 2–43 行：栅格和行内表单排列常用筛选，次要筛选折叠。
- 第 172–185 行：中等密度、带边框表格，接入分页、加载和横向滚动。
- 查询、操作、数据三个区域顺序稳定，适合电脑上的重复查单。

这是对所读页面的观察，不代表已审查整个项目。

## 可以参考

单号、供应商、数量、金额、状态按列对齐；查询条件集中；少量常用操作直接可见。

## 不照搬

蓝色大顶栏、整套 ERP 菜单、多账户和全部高级条件。手机不能直接缩小该表格，应另做单据列表。

源页面虽然出现部分入库状态，但此次未运行它的收货流程，不以它代替我们的分批收货设计。

[返回全部候选](../../README.md) · [来源与使用边界](../sources.md)
