# B：白底与少量强调色

状态：候选，未选定，未实现为可运行模板。

## 真实界面

原项目：[仓图 / WareMap（warehouse）](https://github.com/sunjulei/warehouse/tree/ed5f9a20459ecc79b56d72480bea321fff0d746f)。

### 进货订单

![进货订单](https://raw.githubusercontent.com/sunjulei/warehouse/ed5f9a20459ecc79b56d72480bea321fff0d746f/img/%E8%BF%9B%E8%B4%A7%E7%AE%A1%E7%90%86-%E8%BF%9B%E8%B4%A7%E8%AE%A2%E5%8D%95.png)

### 单据详情

![订单详情](https://raw.githubusercontent.com/sunjulei/warehouse/ed5f9a20459ecc79b56d72480bea321fff0d746f/img/%E8%AE%A2%E5%8D%95%E8%AF%A6%E6%83%85.png)

### 手机工作台

这是原项目的手机图，只供对比。彩色 emoji 网格不是已经选定的手机设计，采购和对账也不等同于这张首页图。

<img src="https://raw.githubusercontent.com/sunjulei/warehouse/ed5f9a20459ecc79b56d72480bea321fff0d746f/img/%E7%A7%BB%E5%8A%A8%E7%AB%AF-%E5%B7%A5%E4%BD%9C%E5%8F%B0.png" alt="原项目移动端工作台" width="380">

## 样式写法观察

- [样式变量](https://github.com/sunjulei/warehouse/blob/ed5f9a20459ecc79b56d72480bea321fff0d746f/warehouse-front/src/styles/variables.scss)：集中定义侧栏、顶栏、字号、间距、圆角和颜色。
- [组件样式](https://github.com/sunjulei/warehouse/blob/ed5f9a20459ecc79b56d72480bea321fff0d746f/warehouse-front/src/styles/element-overrides.scss)：变量接到输入框、按钮和表格，不在每个页面重写整套视觉。
- [手机订单页](https://github.com/sunjulei/warehouse/blob/ed5f9a20459ecc79b56d72480bea321fff0d746f/uniappx/pages/business/inport-order.uvue)：独立使用纵向单据组织单号、状态、金额、时间和操作，没有直接缩小桌面表格。

这是局部源码观察，不表示该项目的所有实现均适合复用。

## 可以参考

白底、浅分隔线、清楚的单据详情分组、统一样式变量。强调色也可再选，不一定采用红色。

## 不照搬

完整菜单、卡片层层包裹、渐变、彩色 emoji、负字距及过小的手机触控区域。
原项目的 API、业务模型及不明确的数据类型不进入新模板。

## 许可注意

[原许可](https://github.com/sunjulei/warehouse/blob/ed5f9a20459ecc79b56d72480bea321fff0d746f/LICENSE) 标题写 MIT，但正文另含未经原作者书面许可不得直接出售的限制。
本候选只记录观察、引用原图，没有复制其代码，不把它描述成标准 MIT 可直接打包复用的模板。

[返回全部候选](../../README.md) · [来源与使用边界](../sources.md)
