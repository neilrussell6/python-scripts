Python Scripts
==============

> A collection of python scripts I've written to perform small tasks in my projects and for educational purposes.

dir-2-es6-export
================

> Creates a JavaScript file containing ES6 exports for all the files in a directory. Works recursively, and allows files to be targeted by extension.

> I write all the content for this website in MarkDown, which I convert to HTML. So I use this script to generate an ES6 export file of those converted HTML files, which is then used to automatically generate the menu on the left and load all the content.

[View code on GitHub](https://github.com/neilrussell6/python-scripts/blob/master/dir-2-js-export/dir-2-js-export.py)

Example usage
-------------

To view usage and all available options / arguments run the following command:

```python
python dir-2-js-export/dir-2-js-export.py -h
```

But for example, if we have the following files in a `./src` directory:

```
./src/html/code-examples.html
./src/html/sub-dir/sub-page.html
./src/html/index.html
```

And we then run the following script:

```bash
python dir-2-js-export.py ./src/html -e html -o ./src/template-map.js -r ./src
```

It will use the names of all the `html` files in `./src/html` to generate `./src/template-map.js`, and will strip `./src` from all the paths, resulting in an export file (`./src/template-map.js`) that looks like this:

```js
import _code_examples from "html/code-examples.html";
import _index from "html/index.html";
import _sub_dir__sub_page from "html/sub-dir/sub-page.html";

const code_examples = { template: _code_examples, label: "Code examples" };
const index = { template: _index, label: "Index" };
const sub_dir__sub_page = { template: _sub_dir__sub_page, label: "Sub page" };

export {
    code_examples,
    index,
    sub_dir__sub_page
};

```

As mentioned above, we can then use this to generate a menu and load content.

Resources
---------

* [pythontips : map_filter](http://book.pythontips.com/en/latest/map_filter.html)
* [argparse docs](https://docs.python.org/2/howto/argparse.html)

search algorithms
=================

> This is a simple script that demonstrates the performance difference of a few different search algorithms when run on an ordered list.

Usage
-----

```
python ordered-search.py [data size]
```

Results
-------

> The output of this script when run on 100 million rows of data (in an array) looks something like this:

| algorithm   		    | data size	| search	| iterations	| seconds
| --------------------------------------------------------------------------------
| linear (for loop)		| 100000000	| 84803807	| 84803807	    | 9.68506
| binary (recursive)    | 100000000	| 84803807	| 23	        | 7.22723
| binary (while loop)	| 100000000	| 84803807	| 23	        | 0.00002

> And these results show that:
> 1. A binary search significantly out performs a linear search.
> 2. A while loop slightly out performs a recursive function.

License
=======

[MIT](https://github.com/neilrussell6/vuejs-markdown-live-reload/blob/master/LICENSE)
