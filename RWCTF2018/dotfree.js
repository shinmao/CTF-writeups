function lls(src) {
    var el = document.createElement('script');
    if (el) {
        el.setAttribute('type', 'text/javascript');
        el.src = src;
        document.body.appendChild(el);
    }
};

function lce(doc, def, parent) {
    var el = null;
    if (typeof doc.createElementNS != "undefined") 
        el = doc.createElementNS("http://www.w3.org/1999/xhtml", def[0]);
    else if (typeof doc.createElement != "undefined") 
        el = doc.createElement(def[0]);

    if (!el) 
        return false;

    for (var i = 1; i < def.length; i++) 
        el.setAttribute(def[i++], def[i]);
    if (parent) 
        parent.appendChild(el);
    return el;
};
window.addEventListener('message', function(e) {
    if (e.data.iframe) {
        if (e.data.iframe && e.data.iframe.value.indexOf('.') == -1 && e.data.iframe.value.indexOf("//") == -1 && e.data.iframe.value.indexOf("。") == -1 && e.data.iframe.value && 
            typeof(e.data.iframe != 'object')) {

            if (e.data.iframe.type == "iframe") {
                lce(doc, ['iframe', 'width', '0', 'height', '0', 'src', e.data.iframe.value], parent);
            } else {
                lls(e.data.iframe.value)
            }
        }
    }
}, false);
window.onload = function(ev) {
    postMessage(JSON.parse(decodeURIComponent(location.search.substr(1))), '*')
}