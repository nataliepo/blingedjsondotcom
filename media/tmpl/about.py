#encoding UTF-8 

#def body

<div class="row">
    <h1>about</h1>
</div>

<div class="row about">
    <p>A long, long, time ago, I wrote a webapp against a service that produced unreliable JSON.  Most of the time, this service's JSON was fine, but, every now and then, it would contain an offensive character invisible to the naked eye, left over from a copy-and-paste job from a well-known word processing app of yore. Tracking down the exact placement of these invisible characters in a hefty set of text proved unwieldy and impossible to those who could not effectively manuever a binary search using <a href="http://www.jsonlint.com">jsonlint.com</a> (an inspiration, btw!) repeatedly. Alas, I wrote this desktop app to quickly, effectively, and blingily help my fellow problem-solvers.</p>

</div>

<div class="row about">

    <p>I'm a developer of a bunch of things, and this is my first foray into Mac Apps after launching <a href="http://29.io/apps">a bunch of iOS apps</a>. Mac Apps are tough!</p>
</div>

<div class="row about">

    <p>Blinged JSON Validator was built and unit-tested against a handful of JSON files. I care about the quality of this app, so, if you feel like the validation of your JSON is incorrect, please <a href="http://gist.github.com">gist</a> a snippet of your JSON and share it on <a href="http://blingedjson.com/support">blingedjson.com/support</a> and I will take a closer look.</p>
</div>

<div class="row about">
    <p>Special thanks to the people who inspired me to solve a sometimes-hard problem with a fun and weird solution!</p>
</div>

<div class="row ">
    
    <p align="center">
        <img src="${ROOT_URL}/static/img/new_diamond_clear.png" width="25px" height="25px" /> <br />
        

        <a href="http://blingedjson.com/support">App Support</a><br />
        <a href="http://nataliepo.com">My Personal Site</a><br />

        <p>Last updated: 03 March 2014</p>
</div>

#end def


#include "media/tmpl/includes/base.py"
