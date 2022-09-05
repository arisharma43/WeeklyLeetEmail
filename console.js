//To get all the links to all the questions, visit this URL 'https://leetcode.com/problemset/algorithms/', open up the dev console and run following code:


var links = document.getElementsByTagName('a');
var all_links =  Array.prototype.slice.call(links);
all_links.forEach(function(val){
    console.log(val.href);
});
