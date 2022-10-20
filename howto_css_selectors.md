# how-to :: CSS selectors
---
## Overview

We care about CSS selectors because they help us differentiate elements in HTML as our pages become more complex.

### Estimated Time Cost: 0.2 hrs

### Prerequisites:

- Know basic HTML styling with CSS
- A web browser to view your amazing styling in action

1. Create a HTML file
2. 
    - Option 1: `<style>` tag in HTML file
    ```html
    <html>
        <head>
            <style>
                <!-- put CSS selectors in here -->
            </style>
        </head>
    </html>
    ```
    - Option 2: Separate CSS file linked
    ```html
    <html>
        <head>
            <link href="[CSS file name]" rel="stylesheet" type="text/css" />
        </head>
    </html>
    ```

### Selector types

|Name|CSS selector|HTML|
|----|------------|----|
|Class|`.class-name`|`class=class-name`|
|ID|`#id-name`|`id=id-name`|
|Type|`type-name`|`<type-name>`|
|Universal|`*`||
|Atrribute|`[attr-name]`|`attr-name=""`|

### Grouping selectors
If you want some selectors to have the same styling, separate them using commas.  
`selector-1, selector2`

### Combinators
|Name|CSS selector|When it styles|
|----|------------|--------------|
|Descendant|`A B`|`B`, if `A` is an ancestor|
|Child|`A > B`|`B`, if `A` is a direct parent|
|General Sibling|`A ~ B`|All instances of `B` after `A`, if `A` and `B` have same parent|
|Adjacent Sibling|`A + B`|`B`, if `A` is right before it and if `A` and `B` have same parent|



3. Inside the `<style>` tags or in the separate CSS file, write
```css
selector-name {
    /* Write styling in here */
    /* Example: */ 
    /* color: red; */
}
```

Put these into your CSS! Enjoy!

### Resources
* [MDN web docs](https://developer.mozilla.org/en-US/docs/Web/CSS/CSS_Selectors)

---

Accurate as of (last update): 2022-10-20

#### Contributors:  
Yuki Feng, pd8  
Maya Mori, pd8  
Eric Sohel, pd8  
Aleksandra Shifrina, pd8  
