参考文档：https://www.jianshu.com/p/d4a1347f467b

实操路程：
D:\Breeze2\breezeApi\src\doc>sphinx-quickstart
Welcome to the Sphinx 1.8.0 quickstart utility.

Please enter values for the following settings (just press Enter to
accept a default value, if one is given in brackets).

Selected root path: .

You have two options for placing the build directory for Sphinx output.
Either, you use a directory "_build" within the root path, or you separate
"source" and "build" directories within the root path.
> Separate source and build directories (y/n) [n]: y

Inside the root directory, two more directories will be created; "_templates"
for custom HTML templates and "_static" for custom stylesheets and other static
files. You can enter another prefix (such as ".") to replace the underscore.
> Name prefix for templates and static dir [_]:

The project name will occur in several places in the built documentation.
> Project name: breeze
> Author name(s): song
> Project release []: 1.0

If the documents are to be written in a language other than English,
you can select a language here by its language code. Sphinx will then
translate text that it generates into that language.

For a list of supported codes, see
http://sphinx-doc.org/config.html#confval-language.
> Project language [en]: zh_CN

The file name suffix for source files. Commonly, this is either ".txt"
or ".rst".  Only files with this suffix are considered documents.
> Source file suffix [.rst]:

One document is special in that it is considered the top node of the
"contents tree", that is, it is the root of the hierarchical structure
of the documents. Normally, this is "index", but if your "index"
document is a custom template, you can also set this to another filename.
> Name of your master document (without suffix) [index]:
Indicate which of the following Sphinx extensions should be enabled:
> autodoc: automatically insert docstrings from modules (y/n) [n]: y
> doctest: automatically test code snippets in doctest blocks (y/n) [n]: y
> intersphinx: link between Sphinx documentation of different projects (y/n) [n]: y
> todo: write "todo" entries that can be shown or hidden on build (y/n) [n]:
> coverage: checks for documentation coverage (y/n) [n]: y
> imgmath: include math, rendered as PNG or SVG images (y/n) [n]:
> mathjax: include math, rendered in the browser by MathJax (y/n) [n]:
> ifconfig: conditional inclusion of content based on config values (y/n) [n]:
> viewcode: include links to the source code of documented Python objects (y/n) [n]: y
> githubpages: create .nojekyll file to publish the document on GitHub pages (y/n) [n]:

A Makefile and a Windows command file can be generated for you so that you
only have to run e.g. `make html' instead of invoking sphinx-build
directly.
> Create Makefile? (y/n) [y]:
> Create Windows command file? (y/n) [y]:

Creating file .\source\conf.py.
Creating file .\source\index.rst.
Creating file .\Makefile.
Creating file .\make.bat.

Finished: An initial directory structure has been created.

You should now populate your master file .\source\index.rst and create other documentation
source files. Use the Makefile to build the docs, like so:
   make builder
where "builder" is one of the supported builders, e.g. html, latex or linkcheck.


D:\Breeze2\breezeApi\src\doc>sphinx-apidoc -o ./source ../../src/
Creating file ./source\demo1.rst.
Creating file ./source\demo2.rst.
Creating file ./source\modules.rst.

D:\Breeze2\breezeApi\src\doc>make html
Running Sphinx v1.8.0
loading translations [zh_CN]... done
making output directory...
loading intersphinx inventory from https://docs.python.org/objects.inv...
WARNING: failed to reach any of the inventories with the following issues:
WARNING: intersphinx inventory 'https://docs.python.org/objects.inv' not fetchable due to <class 'requests.exceptions.ConnectionError'>: ('intersphinx inventory %r not fetchable due to %s: %s', 'https://docs.python.org/objects.inv', <class 'requests.exceptions.ConnectionError'>, ConnectionError(...))
building [mo]: targets for 0 po files that are out of date
building [html]: targets for 4 source files that are out of date
updating environment: 4 added, 0 changed, 0 removed
reading sources... [100%] modules
D:\Breeze2\breezeApi\src\demo1.py:docstring of demo1.Demo1.numpy_style:6: WARNING: Unexpected section title.

Parameters
----------
D:\Breeze2\breezeApi\src\demo1.py:docstring of demo1.Demo1.numpy_style:13: WARNING: Unexpected section title.

Returns
-------
looking for now-outdated files... none found
pickling environment... done
checking consistency... D:\Breeze2\breezeApi\src\doc\source\modules.rst: WARNING: document isn't included in any toctree
done
preparing documents... done
writing output... [100%] modules
generating indices... genindex py-modindex
highlighting module code... [100%] demo2
writing additional pages... search
copying static files... done
copying extra files... done
dumping search index in Chinese (code: zh) ... done
dumping object inventory... done
build succeeded, 5 warnings.

The HTML pages are in build\html.

D:\Breeze2\breezeApi\src\doc>









config.py配置：



