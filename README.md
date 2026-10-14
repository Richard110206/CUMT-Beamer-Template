# CUMT Beamer Template | 中国矿业大学 Beamer 模板

一套以中国矿业大学校园建筑**白描线稿**为背景的 Beamer（LaTeX）演示模板，16:9 横版输出 PDF，配色采用矿大蓝，配合 Claude Code、Codex 等 AI 编程工具可以极速产出演示文稿。

## 效果预览

| 封面 | 正文 |
|:---:|:---:|
| ![封面](pic/readme-cover.png) | ![正文页](pic/readme-content.png) |

| 致谢页 |
|:---:|
| ![致谢页](pic/readme-thanks.png) |

- **封面**：校门牌楼白描背景，配校名标准字
- **正文**：图书馆白描背景（低透明度衬底，不干扰内容）
- **致谢页**：淡蓝校门白描背景，居中显示 Thanks! 与“恳请各位评委批评指正”
- 顶部导航默认包含五个板块：项目背景、研究内容、核心技术、团队成员、应用前景
- 导航圆点每行最多 7 个，超出自动换行；左侧长标题自动适应可用宽度
- 校徽与校名提供 SVG / 矢量 PDF，封面与正文采用蓝白学术配色

## 为什么 2026 年了又把 LaTeX PPT 拿出来做？

说实话，以前手写 Beamer 又累又慢：一行一行敲代码，格式一点点调，做一份 PPT 的时间够用 PowerPoint 做三份。

但现在不一样了——**Claude Code、Codex 这类 AI 编程工具把成本降到了几乎为零**：

- 以前：手动敲 LaTeX、查语法、调格式，累且慢
- 现在：模板放进项目里，让 AI 读你的技术报告和代码，内容填好、格式调好、直接编译出 PDF，自己几乎不用动手

对懒人来说，Beamer 重新变成了做横版 PDF 演示的利器：版式精确、公式漂亮、版本可管理。所以我把它翻出来，重新优化了一遍。

## 相对原版模板的优化

在[学长原版 CUMT Beamer 模板](https://www.overleaf.com/latex/templates/CUMT-beamer-theme/ybqzdsgvrfdq)的基础上：

- 封面、正文、致谢页背景换成本校建筑的**白描线稿**（校门牌楼 + 图书馆），由 AI 生成 PNG；校徽与校名组合图描摹为矢量路径
- 重新设计配色（矿大蓝 `#1A3E8A`）、标题黑体、页眉导航与页脚样式
- 区块（block）、目录页、代码框等页面元素的样式优化

## 推荐工作流：让 AI 帮你做 PPT

1. 把本模板克隆到你的项目里（根目录或子文件夹均可）：

   ```bash
   git clone https://github.com/Richard110206/CUMT-Beamer-Template.git
   ```

2. 在项目目录打开 Claude Code（或 Codex 等 AI 编程工具），让它阅读你的代码和技术文档

3. 一句话下达任务，例如：

   > 参考 CUMT-Beamer-Template/slide.tex 的版式，阅读我的技术报告，帮我生成一份开题汇报的 Beamer 幻灯片。

4. AI 填好内容并自动编译，得到 16:9 横版 PDF —— 完工。

## 编译方法

中文模板，**必须使用 XeLaTeX** 编译，共编译两遍（生成目录与导航）：

```bash
xelatex slide.tex
xelatex slide.tex
```

也可以直接上传 [Overleaf](https://www.overleaf.com)（Menu → Compiler 选择 XeLaTeX）在线编译，无需本地环境。

## 文件结构

```
slide.tex                    # 当前版式示例（封面、目录、正文、致谢等）
CUMT.sty                     # 基础主题：颜色、字体
CUMT-campus.sty              # 校园白描背景主题（当前使用）
slide-before-*.tex           # 设计迭代过程中的历史版本
CUMT-campus-before-*.sty     # 同上
pic/                         # 图片素材（白描背景、校徽、预览图）
ref.bib                      # 参考文献示例
slide.pdf                    # 编译好的效果预览
```

## 致谢

- 感谢学长提供的[原版 CUMT Beamer 模板](https://www.overleaf.com/latex/templates/CUMT-beamer-theme/ybqzdsgvrfdq)
- 白描背景图由 AI 生成，[pic/](pic/) 目录内附生成说明
