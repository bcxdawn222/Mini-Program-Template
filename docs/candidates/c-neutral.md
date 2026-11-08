# C：灰白简洁型

状态：备选。此前由助手选为主方向，后按用户最新选择改为 B；尚未实现为可运行模板。

候选依据：此前明确要求白色、少装饰，业务以采购、库存、出库和对账为主。
保留 C 的观察资料，不代表继续把 C 或原绿色方案作为默认方向。
具体三端边界见 [已选风格与三端规则](../style-direction.md)。

## 真实界面

原项目：[ERPNext](https://github.com/frappe/erpnext/tree/b120a2e81ef017937df2e42912c18404ebadfb3d)。

### 库存汇总

图由该版本 README 链接至官网。图片自身不在该 Git 提交内，可能随官网更新。

![库存汇总](https://erpnext.com/files/v16_stock_summary.png)

### 财务页面

图保存在原仓库固定提交内。仅参考视觉，不代表要增加完整财务模块。

![财务页面](https://raw.githubusercontent.com/frappe/erpnext/b120a2e81ef017937df2e42912c18404ebadfb3d/erpnext/public/images/v16/hero_image.png)

## 图像观察

白色主体、灰色输入框、浅分隔线，主要靠文字粗细和对齐区分层次；颜色较少，不以大块装饰或指标卡作为主要表达。

## 可以参考

采购、库存和对账页面保持素净；重点突出供应商、材料、数量、金额与业务状态。
需要预警时再用明确的状态颜色，不把所有操作都染成同一颜色。

## 不照搬

外文、完整会计及制造流程、复杂菜单。手机需要独立制作中文纵向单据，不把本图当作已完成的手机适配。

本轮没有完成 Frappe 样式框架的源码拆解，没有运行 ERPNext，不能据此宣称已获得可直接复用的同款三端实现。
原项目 [许可文件](https://github.com/frappe/erpnext/blob/b120a2e81ef017937df2e42912c18404ebadfb3d/license.txt) 为 GPL v3；没有将其代码合并到本仓库。

[返回全部候选](../../README.md) · [来源与使用边界](../sources.md)
