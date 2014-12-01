(function(){
/*! NOTE: If you're already including a window.matchMedia polyfill via Modernizr or otherwise, you don't need this part */
;window.matchMedia=window.matchMedia||function(e){"use strict";var t,n=e.documentElement,r=n.firstElementChild||n.firstChild,i=e.createElement("body"),s=e.createElement("div");return s.id="mq-test-1",s.style.cssText="position:absolute;top:-100em",i.style.background="none",i.appendChild(s),function(e){return s.innerHTML='&shy;<style media="'+e+'"> #mq-test-1 { width: 42px; }</style>',n.insertBefore(i,r),t=42===s.offsetWidth,n.removeChild(i),{matches:t,media:e}}}(document),
/*! matchMedia() polyfill - Test a CSS media type/query in JS. Authors & copyright (c) 2012: Scott Jehl, Paul Irish, Nicholas Zakas. Dual MIT/BSD license */
function(e){"use strict";function t(){E(!0)}var n={};if(e.respond=n,n.update=function(){},n.mediaQueriesSupported=e.matchMedia&&e.matchMedia("only all").matches,!n.mediaQueriesSupported){var r,i,s,o=e.document,u=o.documentElement,a=[],f=[],l=[],c={},h=30,p=o.getElementsByTagName("head")[0]||u,d=o.getElementsByTagName("base")[0],v=p.getElementsByTagName("link"),m=[],g=function(){for(var t=0;v.length>t;t++){var n=v[t],r=n.href,i=n.media,s=n.rel&&"stylesheet"===n.rel.toLowerCase();r&&s&&!c[r]&&(n.styleSheet&&n.styleSheet.rawCssText?(b(n.styleSheet.rawCssText,r,i),c[r]=!0):(!/^([a-zA-Z:]*\/\/)/.test(r)&&!d||r.replace(RegExp.$1,"").split("/")[0]===e.location.host)&&m.push({href:r,media:i}))}y()},y=function(){if(m.length){var t=m.shift();S(t.href,function(n){b(n,t.href,t.media),c[t.href]=!0,e.setTimeout(function(){y()},0)})}},b=function(e,t,n){var r=e.match(/@media[^\{]+\{([^\{\}]*\{[^\}\{]*\})+/gi),i=r&&r.length||0;t=t.substring(0,t.lastIndexOf("/"));var s=function(e){return e.replace(/(url\()['"]?([^\/\)'"][^:\)'"]+)['"]?(\))/g,"$1"+t+"$2$3")},o=!i&&n;t.length&&(t+="/"),o&&(i=1);for(var u=0;i>u;u++){var l,c,h,p;o?(l=n,f.push(s(e))):(l=r[u].match(/@media *([^\{]+)\{([\S\s]+?)$/)&&RegExp.$1,f.push(RegExp.$2&&s(RegExp.$2))),h=l.split(","),p=h.length;for(var d=0;p>d;d++)c=h[d],a.push({media:c.split("(")[0].match(/(only\s+)?([a-zA-Z]+)\s?/)&&RegExp.$2||"all",rules:f.length-1,hasquery:c.indexOf("(")>-1,minw:c.match(/\(\s*min\-width\s*:\s*(\s*[0-9\.]+)(px|em)\s*\)/)&&parseFloat(RegExp.$1)+(RegExp.$2||""),maxw:c.match(/\(\s*max\-width\s*:\s*(\s*[0-9\.]+)(px|em)\s*\)/)&&parseFloat(RegExp.$1)+(RegExp.$2||"")})}E()},w=function(){var e,t=o.createElement("div"),n=o.body,r=!1;return t.style.cssText="position:absolute;font-size:1em;width:1em",n||(n=r=o.createElement("body"),n.style.background="none"),n.appendChild(t),u.insertBefore(n,u.firstChild),e=t.offsetWidth,r?u.removeChild(n):n.removeChild(t),e=s=parseFloat(e)},E=function(t){var n="clientWidth",c=u[n],d="CSS1Compat"===o.compatMode&&c||o.body[n]||c,m={},g=v[v.length-1],y=(new Date).getTime();if(t&&r&&h>y-r)return e.clearTimeout(i),i=e.setTimeout(E,h),void 0;r=y;for(var b in a)if(a.hasOwnProperty(b)){var S=a[b],x=S.minw,T=S.maxw,N=null===x,C=null===T,k="em";x&&(x=parseFloat(x)*(x.indexOf(k)>-1?s||w():1)),T&&(T=parseFloat(T)*(T.indexOf(k)>-1?s||w():1)),S.hasquery&&(N&&C||!(N||d>=x)||!(C||T>=d))||(m[S.media]||(m[S.media]=[]),m[S.media].push(f[S.rules]))}for(var L in l)l.hasOwnProperty(L)&&l[L]&&l[L].parentNode===p&&p.removeChild(l[L]);for(var A in m)if(m.hasOwnProperty(A)){var O=o.createElement("style"),M=m[A].join("\n");O.type="text/css",O.media=A,p.insertBefore(O,g.nextSibling),O.styleSheet?O.styleSheet.cssText=M:O.appendChild(o.createTextNode(M)),l.push(O)}},S=function(e,t){var n=x();n&&(n.open("GET",e,!0),n.onreadystatechange=function(){4!==n.readyState||200!==n.status&&304!==n.status||t(n.responseText)},4!==n.readyState&&n.send(null))},x=function(){var t=!1;try{t=new e.XMLHttpRequest}catch(n){t=new e.ActiveXObject("Microsoft.XMLHTTP")}return function(){return t}}();g(),n.update=g,e.addEventListener?e.addEventListener("resize",t,!1):e.attachEvent&&e.attachEvent("onresize",t)}}(this),function(e,t){function n(){var e=v.elements;return"string"==typeof e?e.split(" "):e}function r(e){var t=p[e[c]];return t||(t={},h++,e[c]=h,p[h]=t),t}function i(e,n,i){return n||(n=t),d?n.createElement(e):(i||(i=r(n)),n=i.cache[e]?i.cache[e].cloneNode():f.test(e)?(i.cache[e]=i.createElem(e)).cloneNode():i.createElem(e),n.canHaveChildren&&!a.test(e)?i.frag.appendChild(n):n)}function s(e,t){t.cache||(t.cache={},t.createElem=e.createElement,t.createFrag=e.createDocumentFragment,t.frag=t.createFrag()),e.createElement=function(n){return v.shivMethods?i(n,e,t):t.createElem(n)},e.createDocumentFragment=Function("h,f","return function(){var n=f.cloneNode(),c=n.createElement;h.shivMethods&&("+n().join().replace(/\w+/g,function(e){return t.createElem(e),t.frag.createElement(e),'c("'+e+'")'})+");return n}")(v,t.frag)}function o(e){e||(e=t);var n=r(e);if(v.shivCSS&&!l&&!n.hasCSS){var i,o=e;i=o.createElement("p"),o=o.getElementsByTagName("head")[0]||o.documentElement,i.innerHTML="x<style>article,aside,figcaption,figure,footer,header,hgroup,nav,section{display:block}mark{background:#FF0;color:#000}</style>",i=o.insertBefore(i.lastChild,o.firstChild),n.hasCSS=!!i}return d||s(e,n),e}var u=e.html5||{},a=/^<|^(?:button|map|select|textarea|object|iframe|option|optgroup)$/i,f=/^(?:a|b|code|div|fieldset|h1|h2|h3|h4|h5|h6|i|label|li|ol|p|q|span|strong|style|table|tbody|td|th|tr|ul)$/i,l,c="_html5shiv",h=0,p={},d;(function(){try{var e=t.createElement("a");e.innerHTML="<xyz></xyz>",l="hidden"in e;var n;if(!(n=1==e.childNodes.length)){t.createElement("a");var r=t.createDocumentFragment();n="undefined"==typeof r.cloneNode||"undefined"==typeof r.createDocumentFragment||"undefined"==typeof r.createElement}d=n}catch(i){d=l=!0}})();var v={elements:u.elements||"abbr article aside audio bdi canvas data datalist details figcaption figure footer header hgroup mark meter nav output progress section summary time video",version:"3.6.2pre",shivCSS:!1!==u.shivCSS,supportsUnknownElements:d,shivMethods:!1!==u.shivMethods,type:"default",shivDocument:o,createElement:i,createDocumentFragment:function(e,i){e||(e=t);if(d)return e.createDocumentFragment();for(var i=i||r(e),s=i.frag.cloneNode(),o=0,u=n(),a=u.length;o<a;o++)s.createElement(u[o]);return s}};e.html5=v,o(t)}(this
,document)}).call(this);
