import marimo

__generated_with = "0.9.14"
app = marimo.App(width="medium")


@app.cell
def __():
    import pandas as pd
    import marimo as mo
    import patchworklib as pw
    return mo, pd, pw


@app.cell(hide_code=True)
def __(mo):
    mo.md("""# First steps""")
    return


@app.cell(hide_code=True)
def __(mo):
    mo.md(
        """
        ## Introduction

        The goal of this chapter is to teach you how to produce useful graphics with ggplot2 as quickly as possible.
        You'll learn the basics of `ggplot()` along with some useful "recipes" to make the most important plots.
        `ggplot()` allows you to make complex plots with just a few lines of code because it's based on a rich underlying theory, the grammar of graphics.
        Here we'll skip the theory and focus on the practice, and in later chapters you'll learn how to use the full expressive power of the grammar.

        In this chapter you'll learn:

        -   About the `mpg` dataset included with ggplot2, @sec-fuel-economy-data.

        -   The three key components of every plot: data, aesthetics and geoms, @sec-basic-use.

        -   How to add additional variables to a plot with aesthetics, @sec-aesthetics.

        -   How to display additional categorical variables in a plot using small multiples created by faceting, @sec-qplot-faceting.

        -   A variety of different geoms that you can use to create different types of plots, @sec-plot-geoms.

        -   How to modify the axes, @sec-axes.

        -   Things you can do with a plot object other than display it, like save it to disk, @sec-output.
        """
    )
    return


@app.cell(hide_code=True)
def __(mo):
    mo.md(
        """
        ## Fuel economy data

        In this chapter, we'll mostly use one data set that's bundled with ggplot2: `mpg`.
        It includes information about the fuel economy of popular car models in 1999 and 2008, collected by the US Environmental Protection Agency, <http://fueleconomy.gov>.
        You can access the data by loading ggplot2
        """
    )
    return


@app.cell
def __():
    from plotnine import ggplot, geom_point, aes, geom_line, geom_histogram, facet_wrap
    from plotnine.data import mpg
    return (
        aes,
        facet_wrap,
        geom_histogram,
        geom_line,
        geom_point,
        ggplot,
        mpg,
    )


@app.cell
def __(mpg):
    mpg
    return


@app.cell(hide_code=True)
def __(mo):
    mo.md(
        r"""
        The variables are mostly self-explanatory:

        -   `cty` and `hwy` record miles per gallon (mpg) for city and highway driving.

        -   `displ` is the engine displacement in litres.

        -   `drv` is the drivetrain: front wheel (f), rear wheel (r) or four wheel (4).

        -   `model` is the model of car.
            There are 38 models, selected because they had a new edition every year between 1999 and 2008.

        -   `class` is a categorical variable describing the "type" of car: two seater, SUV, compact, etc.

        This dataset suggests many interesting questions.
        How are engine size and fuel economy related?
        Do certain manufacturers care more about fuel economy than others?
        Has fuel economy improved in the last ten years?
        We will try to answer some of these questions, and in the process learn how to create some basic plots with ggplot2.
        """
    )
    return


@app.cell(hide_code=True)
def __(mo):
    mo.md(
        r"""
        ### Exercises

        1.  List five functions that you could use to get more information about the `mpg` dataset.

        2.  How can you find out what other datasets are included with ggplot2?

        3.  Apart from the US, most countries use fuel consumption (fuel consumed over fixed distance) rather than fuel economy (distance travelled with fixed amount of fuel).
            How could you convert `cty` and `hwy` into the European standard of l/100km?

        4.  Which manufacturer has the most models in this dataset?
            Which model has the most variations?
            Does your answer change if you remove the redundant specification of drive train (e.g. "pathfinder 4wd", "a4 quattro") from the model name?
        """
    )
    return


@app.cell(hide_code=True)
def __(mo):
    mo.md(
        r"""
        ## Key components
        Every ggplot2 plot has three key components:

        1.  **data**,

        2.  A set of **aesthetic mappings** between variables in the data and visual properties, and

        3.  At least one layer which describes how to render each observation.
            Layers are usually created with a **geom** function.

        Here's a simple example:
        """
    )
    return


@app.cell
def __(aes, geom_point, ggplot, mpg):
    (ggplot(mpg, aes(x="displ", y="hwy")) + geom_point()).show()
    return


@app.cell(hide_code=True)
def __(mo):
    mo.md(
        """
        This produces a scatterplot defined by:

        1.  Data: `mpg`.
        2.  Aesthetic mapping: engine size mapped to x position, fuel economy to y position.
        3.  Layer: points.

        Pay attention to the structure of this function call: data and aesthetic mappings are supplied in `ggplot()`, then layers are added on with `+`.
        This is an important pattern, and as you learn more about ggplot2 you'll construct increasingly sophisticated plots by adding on more types of components.

        Almost every plot maps a variable to `x` and `y`, so naming these aesthetics is tedious, so the first two unnamed arguments to `aes()` will be mapped to `x` and `y`.
        This means that the following code is identical to the example above:
        """
    )
    return


@app.cell
def __(aes, geom_point, ggplot, mpg):
    (ggplot(mpg, aes("displ", "hwy")) + geom_point()).show()
    return


@app.cell(hide_code=True)
def __(mo):
    mo.md(
        r"""
        We'll stick to that style throughout the book, so don't forget that the first two arguments to `aes()` are `x` and `y`.
        Note that we've put each command on a new line.
        We recommend doing this in your own code, so it's easy to scan a plot specification and see exactly what's there.
        In this chapter, we'll sometimes use just one line per plot, because it makes it easier to see the differences between plot variations.

        The plot shows a strong correlation: as the engine size gets bigger, the fuel economy gets worse.
        There are also some interesting outliers: some cars with large engines get higher fuel economy than average.
        What sort of cars do you think they are?
        """
    )
    return


@app.cell(hide_code=True)
def __(mo):
    mo.md(
        r"""
        ### Exercises

        1.  How would you describe the relationship between `cty` and `hwy`?
            Do you have any concerns about drawing conclusions from that plot?

        2.  What does `ggplot(mpg, aes(model, manufacturer)) + geom_point()` show?
            Is it useful?
            How could you modify the data to make it more informative?

        3.  Describe the data, aesthetic mappings and layers used for each of the following plots.
            You'll need to guess a little because you haven't seen all the datasets and functions yet, but use your common sense!
            See if you can predict what the plot will look like before running the code.

            1.  `ggplot(mpg, aes(cty, hwy)) + geom_point()`
            2.  `ggplot(diamonds, aes(carat, price)) + geom_point()`
            3.  `ggplot(economics, aes(date, unemploy)) + geom_line()`
            4.  `ggplot(mpg, aes(cty)) + geom_histogram()`
        """
    )
    return


@app.cell(hide_code=True)
def __(mo):
    mo.md("""#### 2""")
    return


@app.cell
def __(aes, geom_point, ggplot, mpg):
    (ggplot(mpg, aes("model", "manufacturer")) + geom_point()).show()
    return


@app.cell
def __(mo):
    mo.md(r"""#### 3""")
    return


@app.cell
def __():
    from plotnine.data import diamonds, economics
    return diamonds, economics


@app.cell
def __(aes, geom_point, ggplot, mpg):
    (ggplot(mpg, aes("cty", "hwy")) + geom_point()).show()
    return


@app.cell
def __(aes, diamonds, geom_point, ggplot):
    (ggplot(diamonds, aes("carat", "price")) + geom_point()).show()
    return


@app.cell
def __(aes, economics, geom_line, ggplot):
    (ggplot(economics, aes("date", "unemploy")) + geom_line()).show()
    return


@app.cell
def __(aes, geom_histogram, ggplot, mpg):
    (ggplot(mpg, aes("cty")) + geom_histogram()).show()
    return


@app.cell(hide_code=True)
def __(mo):
    mo.md(
        """
        ## Colour, size, shape and other aesthetic attributes {#sec-aesthetics}

        To add additional variables to a plot, we can use other aesthetics like colour, shape, and size (NB: while we use British spelling throughout this book, ggplot2 also accepts American spellings).
        These work in the same way as the `x` and `y` aesthetics, and are added into the call to `aes()`: \index{Aesthetics} \indexf{aes}

        -   `aes(displ, hwy, colour = class)`
        -   `aes(displ, hwy, shape = drv)`
        -   `aes(displ, hwy, size = cyl)`

        ggplot2 takes care of the details of converting data (e.g., 'f', 'r', '4') into aesthetics (e.g., 'red', 'yellow', 'green') with a **scale**.
        There is one scale for each aesthetic mapping in a plot.
        The scale is also responsible for creating a guide, an axis or legend, that allows you to read the plot, converting aesthetic values back into data values.
        For now, we'll stick with the default scales provided by ggplot2.
        You'll learn how to override them in @sec-scale-colour.

        To learn more about those outlying variables in the previous scatterplot, we could map the class variable to colour:
        """
    )
    return


@app.cell
def __(aes, geom_point, ggplot, mpg):
    (ggplot(mpg, aes("displ", "hwy", colour="class")) + geom_point()).show()
    return


@app.cell(hide_code=True)
def __(mo):
    mo.md(
        """
        This gives each point a unique colour corresponding to its class.
        The legend allows us to read data values from the colour, showing us that the group of cars with unusually high fuel economy for their engine size are two seaters: cars with big engines, but lightweight bodies.

        If you want to set an aesthetic to a fixed value, without scaling it, do so in the individual layer outside of `aes()`.
        Compare the following two plots: \index{Aesthetics!setting}
        """
    )
    return


@app.cell
def __(aes, geom_point, ggplot, mpg):
    (ggplot(mpg, aes("displ", "hwy")) + geom_point(aes(colour="blue"))).show()
    return


@app.cell
def __(aes, geom_point, ggplot, mpg):
    (ggplot(mpg, aes("displ", "hwy")) + geom_point(colour="blue")).show()
    return


@app.cell(hide_code=True)
def __(mo):
    mo.md(
        """
        In the first plot, the value "blue" is scaled to a pinkish colour, and a legend is added.
        In the second plot, the points are given the R colour blue.
        This is an important technique and you'll learn more about it in @sec-setting-mapping.
        See `vignette("ggplot2-specs")` for the values needed for colour and other aesthetics.

        Different types of aesthetic attributes work better with different types of variables.
        For example, colour and shape work well with categorical variables, while size works well for continuous variables.
        The amount of data also makes a difference: if there is a lot of data it can be hard to distinguish different groups.
        An alternative solution is to use faceting, as described next.

        When using aesthetics in a plot, less is usually more.
        It's difficult to see the simultaneous relationships among colour and shape and size, so exercise restraint when using aesthetics.
        Instead of trying to make one very complex plot that shows everything at once, see if you can create a series of simple plots that tell a story, leading the reader from ignorance to knowledge.
        """
    )
    return


@app.cell(hide_code=True)
def __(mo):
    mo.md(
        """
        ### Exercises

        1.  Experiment with the colour, shape and size aesthetics.
            What happens when you map them to continuous values?
            What about categorical values?
            What happens when you use more than one aesthetic in a plot?

        2.  What happens if you map a continuous variable to shape?
            Why?
            What happens if you map `trans` to shape?
            Why?

        3.  How is drive train related to fuel economy?
            How is drive train related to engine size and class?
        """
    )
    return


@app.cell(hide_code=True)
def __(mo):
    mo.md("""#### 1""")
    return


@app.cell
def __(aes, geom_point, ggplot, mpg):
    # continuous
    (ggplot(mpg, aes("displ", "hwy", colour="cty")) + geom_point()).show()
    return


@app.cell
def __(aes, geom_point, ggplot, mpg):
    # categorical
    (ggplot(mpg, aes("displ", "hwy", colour="model")) + geom_point()).show()
    return


@app.cell
def __(aes, geom_point, ggplot, mpg):
    # use more than one aesthetic in a plot
    (
        ggplot(mpg, aes("displ", "hwy", colour="cty")) + geom_point(aes(colour="model"))
    ).show()
    return


@app.cell
def __(mo):
    mo.md("""#### 2""")
    return


@app.cell
def __(aes, geom_point, ggplot, mpg):
    # map a continuous variable to shape
    (ggplot(mpg, aes("displ", "hwy", shape="cty")) + geom_point()).show()
    return


@app.cell
def __(aes, geom_point, ggplot, mpg):
    # map `trans` to shape
    (ggplot(mpg, aes("displ", "hwy", shape="trans")) + geom_point()).show()
    return


@app.cell
def __(mo):
    mo.md("""#### 3""")
    return


@app.cell
def __(aes, geom_point, ggplot, mpg):
    (ggplot(mpg, aes("cty", "hwy", color="drv")) + geom_point()).show()
    return


@app.cell
def __(aes, geom_point, ggplot, mpg):
    (ggplot(mpg, aes("displ", "class", color="drv")) + geom_point()).show()
    return


@app.cell(hide_code=True)
def __(mo):
    mo.md(
        """
        ## Faceting {#sec-qplot-faceting}

        Another technique for displaying additional categorical variables on a plot is faceting.
        Faceting creates tables of graphics by splitting the data into subsets and displaying the same graph for each subset.
        You'll learn more about faceting in @sec-facet, but it's such a useful technique that you need to know it right away.
        \index{Faceting}

        There are two types of faceting: grid and wrapped.
        Wrapped is the most useful, so we'll discuss it here, and you can learn about grid faceting later.
        To facet a plot you simply add a faceting specification with `facet_wrap()`, which takes the name of a variable preceded by `~`.
        \indexf{facet\_wrap}
        """
    )
    return


@app.cell
def __(aes, facet_wrap, geom_point, ggplot, mpg):
    (ggplot(mpg, aes("displ", "hwy")) + geom_point() + facet_wrap("~class")).show()
    return


@app.cell(hide_code=True)
def __(mo):
    mo.md(
        """
        You might wonder when to use faceting and when to use aesthetics.
        You'll learn more about the relative advantages and disadvantages of each in @sec-group-vs-facet.
        """
    )
    return


@app.cell(hide_code=True)
def __(mo):
    mo.md(
        """
        ### Exercises

        1.  What happens if you try to facet by a continuous variable like `hwy`?
            What about `cyl`?
            What's the key difference?

        2.  Use faceting to explore the 3-way relationship between fuel economy, engine size, and number of cylinders.
            How does faceting by number of cylinders change your assessement of the relationship between engine size and fuel economy?

        3.  Read the documentation for `facet_wrap()`.
            What arguments can you use to control how many rows and columns appear in the output?

        4.  What does the `scales` argument to `facet_wrap()` do?
            When might you use it?
        """
    )
    return


@app.cell(hide_code=True)
def __(mo):
    mo.md("""#### 1""")
    return


@app.cell
def __(aes, facet_wrap, geom_point, ggplot, mpg):
    (ggplot(mpg, aes("displ", "cty")) + geom_point() + facet_wrap("~hwy")).show()
    return


@app.cell
def __(aes, facet_wrap, geom_point, ggplot, mpg):
    (ggplot(mpg, aes("displ", "cty")) + geom_point() + facet_wrap("hwy")).show()
    return


@app.cell
def __(aes, facet_wrap, geom_point, ggplot, mpg):
    (ggplot(mpg, aes("displ", "cty")) + geom_point() + facet_wrap("~cyl")).show()
    return


@app.cell(hide_code=True)
def __(mo):
    mo.md("""#### 2""")
    return


@app.cell
def __(aes, facet_wrap, geom_point, ggplot, mpg):
    (ggplot(mpg, aes("displ", "hwy")) + geom_point() + facet_wrap("~cyl")).show()
    return


@app.cell(hide_code=True)
def __(mo):
    mo.md("""#### 4""")
    return


@app.cell
def __(aes, facet_wrap, geom_point, ggplot, mpg):
    (
        ggplot(mpg, aes("displ", "hwy"))
        + geom_point()
        + facet_wrap("~cyl", scales="free")
    ).show()
    return


@app.cell(hide_code=True)
def __(mo):
    mo.md(
        """
        ## Plot geoms {#sec-plot-geoms}

        You might guess that by substituting `geom_point()` for a different geom function, you'd get a different type of plot.
        That's a great guess!
        In the following sections, you'll learn about some of the other important geoms provided in ggplot2.
        This isn't an exhaustive list, but should cover the most commonly used plot types.
        You'll learn more in @sec-individual-geoms and @sec-collective-geoms.

        -   `geom_smooth()` fits a smoother to the data and displays the smooth and its standard error.

        -   `geom_boxplot()` produces a box-and-whisker plot to summarise the distribution of a set of points.

        -   `geom_histogram()` and `geom_freqpoly()` show the distribution of continuous variables.

        -   `geom_bar()` shows the distribution of categorical variables.

        -   `geom_path()` and `geom_line()` draw lines between the data points.
            A line plot is constrained to produce lines that travel from left to right, while paths can go in any direction.
            Lines are typically used to explore how things change over time.
        """
    )
    return


@app.cell
def __():
    from plotnine import geom_smooth, geom_boxplot, geom_bar, geom_path
    return geom_bar, geom_boxplot, geom_path, geom_smooth


@app.cell(hide_code=True)
def __(mo):
    mo.md(
        """
        ### Adding a smoother to a plot {#sec-smooth}

        If you have a scatterplot with a lot of noise, it can be hard to see the dominant pattern.
        In this case it's useful to add a smoothed line to the plot with `geom_smooth()`: \index{Smoothing} \indexf{geom\_smoothh
        """
    )
    return


@app.cell
def __(aes, geom_point, geom_smooth, ggplot, mpg):
    (ggplot(mpg, aes("displ", "hwy")) + geom_point() + geom_smooth()).show()
    return


@app.cell(hide_code=True)
def __(mo):
    mo.md(
        """
        This overlays the scatterplot with a smooth curve, including an assessment of uncertainty in the form of point-wise confidence intervals shown in grey.
        If you're not interested in the confidence interval, turn it off with `geom_smooth(se = FALSE)`.

        An important argument to `geom_smooth()` is the `method`, which allows you to choose which type of model is used to fit the smooth curve:

        -   `method = "loess"`, the default for small n, uses a smooth local regression (as described in `?loess`).
            The wiggliness of the line is controlled by the `span` parameter, which ranges from 0 (exceedingly wiggly) to 1 (not so wiggly).
        """
    )
    return


@app.cell
def __(aes, geom_point, geom_smooth, ggplot, mpg):
    (ggplot(mpg, aes("displ", "hwy")) + geom_point() + geom_smooth(span=0.2)).show()
    return


@app.cell
def __(aes, geom_point, geom_smooth, ggplot, mpg):
    (ggplot(mpg, aes("displ", "hwy")) + geom_point() + geom_smooth(span=1)).show()
    return


@app.cell(hide_code=True)
def __(mo):
    mo.md(
        """
        Loess does not work well for large datasets (it's $O(n^2)$ in memory), so an alternative smoothing algorithm is used when $n$ is greater than 1,000.

        -   `method = "gam"` fits a generalised additive model provided by the **mgcv** package.
            You need to first load mgcv, then use a formula like `formula = y ~ s(x)` or `y ~ s(x, bs = "cs")` (for large data).
            This is what ggplot2 uses when there are more than 1,000 points.
            \index{mgcv}
        """
    )
    return


@app.cell
def __(aes, geom_point, geom_smooth, ggplot, mpg):
    (ggplot(mpg, aes("displ", "hwy")) + geom_point() + geom_smooth(method="gam")).show()
    return


@app.cell(hide_code=True)
def __(mo):
    mo.md("""-   `method = "lm"` fits a linear model, giving the line of best fit.""")
    return


@app.cell
def __(aes, geom_point, geom_smooth, ggplot, mpg):
    (ggplot(mpg, aes("displ", "hwy")) + geom_point() + geom_smooth(method="lm")).show()
    return


@app.cell(hide_code=True)
def __(mo):
    mo.md(
        """
        -   `method = "rlm"` works like `lm()`, but uses a robust fitting algorithm so that outliers don't affect the fit as much.
            It's part of the **MASS** package, so remember to load that first.
            \index{MASS}
        """
    )
    return


@app.cell
def __(aes, geom_point, geom_smooth, ggplot, mpg):
    (ggplot(mpg, aes("displ", "hwy")) + geom_point() + geom_smooth(method="rlm")).show()
    return


@app.cell(hide_code=True)
def __(mo):
    mo.md(
        """
        ### Boxplots and jittered points {#sec-boxplot}

        When a set of data includes a categorical variable and one or more continuous variables, you will probably be interested to know how the values of the continuous variables vary with the levels of the categorical variable.
        Say we're interested in seeing how fuel economy varies within cars that have the same kind of drivetrain.
        We might start with a scatterplot like this:
        """
    )
    return


@app.cell
def __(aes, geom_point, ggplot, mpg):
    (ggplot(mpg, aes("drv", "hwy")) + geom_point()).show()
    return


@app.cell(hide_code=True)
def __(mo):
    mo.md(
        """
        Because there are few unique values of both `drv` and `hwy`, there is a lot of overplotting.
        Many points are plotted in the same location, and it's difficult to see the distribution.
        There are three useful techniques that help alleviate the problem:

        -   Jittering, `geom_jitter()`, adds a little random noise to the data which can help avoid overplotting.
            \index{Jittering} \indexf{geom\_jitter}

        -   Boxplots, `geom_boxplot()`, summarise the shape of the distribution with a handful of summary statistics.
            \index{Boxplot} \indexf{geom\_boxplot}

        -   Violin plots, `geom_violin()`, show a compact representation of the "density" of the distribution, highlighting the areas where more points are found.
            \index{Violin plot} \indexf{geom\_violin}

        These are illustrated below:
        """
    )
    return


@app.cell
def __():
    from plotnine import geom_jitter, geom_violin
    return geom_jitter, geom_violin


@app.cell
def __(aes, geom_jitter, ggplot, mpg):
    (ggplot(mpg, aes("drv", "hwy")) + geom_jitter()).show()
    return


@app.cell
def __(aes, geom_boxplot, ggplot, mpg):
    (ggplot(mpg, aes("drv", "hwy")) + geom_boxplot()).show()
    return


@app.cell
def __(aes, geom_violin, ggplot, mpg):
    (ggplot(mpg, aes("drv", "hwy")) + geom_violin()).show()
    return


@app.cell(hide_code=True)
def __(mo):
    mo.md(
        """
        Each method has its strengths and weaknesses.
        Boxplots summarise the bulk of the distribution with only five numbers, while jittered plots show every point but only work with relatively small datasets. 
        Violin plots give the richest display, but rely on the calculation of a density estimate, which can be hard to interpret.

        For jittered points, `geom_jitter()` offers the same control over aesthetics as `geom_point()`: `size`, `colour`, and `shape`.
        For `geom_boxplot()` and `geom_violin()`, you can control the outline `colour` or the internal `fill` colour.
        """
    )
    return


@app.cell(hide_code=True)
def __(aes, geom_boxplot, geom_jitter, geom_violin, ggplot, mpg):
    (
        ggplot(mpg, aes("drv", "hwy")) 
        + geom_violin(style="left")
        + geom_boxplot()
        + geom_jitter()
    ).show()
    return


@app.cell(hide_code=True)
def __(mo):
    mo.md(
        """
        ### Histograms and frequency polygons {#sec-distribution}

        Histograms and frequency polygons show the distribution of a single numeric variable.
        They provide more information about the distribution of a single group than boxplots do, at the expense of needing more space.
        \index{Histogram} \indexf{geom\_histogram}
        """
    )
    return


@app.cell
def __():
    from plotnine import geom_freqpoly
    return (geom_freqpoly,)


@app.cell
def __(aes, geom_histogram, ggplot, mpg):
    (ggplot(mpg, aes("hwy")) + geom_histogram()).show()
    return


@app.cell
def __(aes, geom_freqpoly, ggplot, mpg):
    (ggplot(mpg, aes("hwy")) + geom_freqpoly()).show()
    return


@app.cell(hide_code=True)
def __(mo):
    mo.md(
        """
        Both histograms and frequency polygons work in the same way: they bin the data, then count the number of observations in each bin.
        The only difference is the display: histograms use bars and frequency polygons use lines.

        You can control the width of the bins with the `binwidth` argument (if you don't want evenly spaced bins you can use the `breaks` argument).
        It is **very important** to experiment with the bin width.
        The default just splits your data into 30 bins, which is unlikely to be the best choice.
        You should always try many bin widths, and you may find you need multiple bin widths to tell the full story of your data.
        """
    )
    return


@app.cell
def __(aes, geom_freqpoly, ggplot, mpg, pw):
    g1=pw.load_ggplot((ggplot(mpg, aes("hwy")) + geom_freqpoly(binwidth=2.5)))
    g2=pw.load_ggplot((ggplot(mpg, aes("hwy")) + geom_freqpoly(binwidth=1)))
    (g1|g2)
    return g1, g2


@app.cell(hide_code=True)
def __(mo):
    mo.md(
        """
        ### Bar charts {#sec-bar}

        The discrete analogue of the histogram is the bar chart, `geom_bar()`.
        It's easy to use: \index{Barchart} \indexf{geom\_bar}
        """
    )
    return


@app.cell
def __(aes, geom_bar, ggplot, mpg):
    (ggplot(mpg, aes("manufacturer")) + geom_bar()).show()
    return


@app.cell(hide_code=True)
def __(mo):
    mo.md(
        """
        (You'll learn how to fix the labels in @sec-theme-axis).

        Bar charts can be confusing because there are two rather different plots that are both commonly called bar charts.
        The above form expects you to have unsummarised data, and each observation contributes one unit to the height of each bar.
        The other form of bar chart is used for presummarised data.
        For example, you might have three drugs with their average effect:
        """
    )
    return


@app.cell
def __(pd):
    drugs = pd.DataFrame(
        data={
            "drug": ["a", "b", "c"],
            "effect": [4.2, 9.7, 6.1]
        }
    )
    drugs
    return (drugs,)


@app.cell(hide_code=True)
def __(mo):
    mo.md(
        """
        To display this sort of data, you need to tell `geom_bar()` to not run the default stat which bins and counts the data.
        However, we think it's even better to use `geom_point()` because points take up less space than bars, and don't require that the y axis includes 0.
        """
    )
    return


@app.cell
def __(aes, drugs, geom_bar, geom_point, ggplot, pw):
    (
        pw.load_ggplot((ggplot(drugs, aes("drug", "effect")) + geom_bar(stat="identity"))) | 
        pw.load_ggplot((ggplot(drugs, aes("drug", "effect")) + geom_point()))
    )
    return


@app.cell(hide_code=True)
def __(mo):
    mo.md(
        r"""
        ### Time series with line and path plots {#sec-line}

        Line and path plots are typically used for time series data.
        Line plots join the points from left to right, while path plots join them in the order that they appear in the dataset (in other words, a line plot is a path plot of the data sorted by x value).
        Line plots usually have time on the x-axis, showing how a single variable has changed over time.
        Path plots show how two variables have simultaneously changed over time, with time encoded in the way that observations are connected.

        Because the year variable in the `mpg` dataset only has two values, we'll show some time series plots using the `economics` dataset, which contains economic data on the US measured over the last 40 years.
        The figure below shows two plots of unemployment over time, both produced using `geom_line()`.
        The first shows the unemployment rate while the second shows the median number of weeks unemployed.
        We can already see some differences in these two variables, particularly in the last peak, where the unemployment percentage is lower than it was in the preceding peaks, but the length of unemployment is high.
        \indexf{geom\_line} \indexf{geom\_path} \index{Data!economics@\texttt{economics}}
        """
    )
    return


@app.cell
def __(economics):
    economics
    return


@app.cell
def __(aes, economics, geom_path, geom_point, ggplot, pd, pw):
    economics['year'] = pd.to_datetime(economics['date']).dt.year
    (
        pw.load_ggplot(
            ggplot(economics, aes("unemploy / pop", "uempmed"))
            + geom_path()
            + geom_point()
        ) |
        pw.load_ggplot(
            ggplot(economics, aes("unemploy / pop", "uempmed"))
            + geom_path(colour="grey")
            + geom_point(aes(colour = "year"))
        )
    )
    return


@app.cell(hide_code=True)
def __(mo):
    mo.md(
        """
        We can see that unemployment rate and length of unemployment are highly correlated, but in recent years the length of unemployment has been increasing relative to the unemployment rate.

        With longitudinal data, you often want to display multiple time series on each plot, each series representing one individual.
        To do this you need to map the `group` aesthetic to a variable encoding the group membership of each observation.
        This is explained in more depth in @sec-collective-geoms.
        \index{Longitudinal data|see{Data, longitudinal}} \index{Data!longitudinal}
        """
    )
    return


@app.cell(hide_code=True)
def __(mo):
    mo.md(
        """
        ### Exercises

        1.  What's the problem with the plot created by `ggplot(mpg, aes(cty, hwy)) + geom_point()`?
            Which of the geoms described above is most effective at remedying the problem?

        2.  One challenge with `ggplot(mpg, aes(class, hwy)) + geom_boxplot()` is that the ordering of `class` is alphabetical, which is not terribly useful.
            How could you change the factor levels to be more informative?

            Rather than reordering the factor by hand, you can do it automatically based on the data: `ggplot(mpg, aes(reorder(class, hwy), hwy)) + geom_boxplot()`.
            What does `reorder()` do?
            Read the documentation.

        3.  Explore the distribution of the carat variable in the `diamonds` dataset.
            What binwidth reveals the most interesting patterns?

        4.  Explore the distribution of the price variable in the `diamonds` data.
            How does the distribution vary by cut?

        5.  You now know (at least) three ways to compare the distributions of subgroups: `geom_violin()`, `geom_freqpoly()` and the colour aesthetic, or `geom_histogram()` and faceting.
            What are the strengths and weaknesses of each approach?
            What other approaches could you try?

        6.  Read the documentation for `geom_bar()`.
            What does the `weight` aesthetic do?

        7.  Using the techniques already discussed in this chapter, come up with three ways to visualise a 2d categorical distribution.
            Try them out by visualising the distribution of `model` and `manufacturer`, `trans` and `class`, and `cyl` and `trans`.
        """
    )
    return


@app.cell
def __(mo):
    mo.md(""" """)
    return


@app.cell
def __(aes, geom_jitter, geom_point, ggplot, mpg, pw):
    # 1
    # problem: overlapping data points?
    (
        pw.load_ggplot(ggplot(mpg, aes("cty", "hwy")) + geom_point())
        | pw.load_ggplot(ggplot(mpg, aes("cty", "hwy")) + geom_point() + geom_jitter())
    )
    return


@app.cell
def __():
    return


@app.cell
def __(aes, geom_boxplot, ggplot, mpg):

    (
        ggplot(mpg, aes("class", "hwy")) + geom_boxplot()
    )
    return


if __name__ == "__main__":
    app.run()
