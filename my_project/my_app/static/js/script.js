function handleFiles(event) {
    var file = event.target.files[0];
    console.log("Upload:", file);
    if (file == undefined)
        return;
    var xhr = new XMLHttpRequest();
    (xhr.upload || xhr).addEventListener('progress', function (event) {
        var done = event.position || event.loaded;
        var total = event.totalSize || event.total;
        console.log('xhr progress: ' + Math.round(done / total * 100) + "%");
        // var progress_bar = document.getElementById('progress_file');
        // progress_bar.style.width = (Math.round(done / total * 100)) + "%";
    });
    xhr.onreadystatechange = function () {
        if (xhr.readyState == 4 && xhr.status == 200) {
            console.log(xhr.responseText);
        }
    };
    xhr.open('post', 'sendfile', true);
    var fd = new FormData();
    fd.append('filename', file.name);
    fd.append('file', file);
    xhr.send(fd);

    var newdocument = document.createElement('li');
    newdocument.setAttribute("class", "row-document");
    newdocument.setAttribute("onclick", "row_document_click(event)");
    newdocument.innerHTML = file.name;
    document.getElementById('ul-scroll').appendChild(newdocument);
}

function row_document_click(event) {
    console.log('Click row: ', event.target.innerHTML);
    var xhr = new XMLHttpRequest();
    xhr.onreadystatechange = function () {
        if (xhr.readyState == 4 && xhr.status == 200) {
            //console.log(xhr.responseText);
            //document.getElementById("div_show").appendChild(xhr.responseText);
            var parser = new DOMParser();
            var doc = parser.parseFromString(xhr.responseText, "text/xml");
            //document.getElementById("div_show").appendChild(doc.firstChild);
            var myNode = document.getElementById("div_show");
            while (myNode.firstChild) {
                myNode.removeChild(myNode.firstChild);
            }
            myNode.insertAdjacentHTML('afterend', xhr.responseText);
            var table = document.getElementById("div-document-table");
            table.parentNode.removeChild(table);
            myNode.appendChild(table);
        }
    };
    xhr.open('post', 'getdocument', true);
    var fd = new FormData();
    fd.append('name', event.target.innerHTML);
    xhr.send(fd);
}

function showDocuments() {
    console.log('Show documents request: ');
    var xhr = new XMLHttpRequest();
    xhr.onreadystatechange = function () {
        console.log('Ei\n', xhr.status);
        if (xhr.readyState == 4 && xhr.status == 200) {
            console.log('oi\n', xhr.response);
            var parser = new DOMParser();

            var myNode = document.getElementById("div_show");
            while (myNode.firstChild) {
                myNode.removeChild(myNode.firstChild);
            }

            myNode.insertAdjacentHTML('afterend', xhr.responseText);
            var table = document.getElementById("div-tables");
            table.parentNode.removeChild(table);
            myNode.appendChild(table);
        }
    };
    xhr.open('post', 'getglobal', true);
    var fd = new FormData();
    fd.append('request', 'showDocuments');
    xhr.send(fd);
}

function showIdf() {
    console.log('Show idf request: ');
    var xhr = new XMLHttpRequest();
    xhr.onreadystatechange = function () {
        console.log('Ei\n', xhr.status);
        if (xhr.readyState == 4 && xhr.status == 200) {
            console.log('oi\n', xhr.response);
            var parser = new DOMParser();

            var myNode = document.getElementById("div_show");
            while (myNode.firstChild) {
                myNode.removeChild(myNode.firstChild);
            }

            myNode.insertAdjacentHTML('afterend', xhr.responseText);
            var table = document.getElementById("div-document-table");
            table.parentNode.removeChild(table);
            myNode.appendChild(table);
        }
    };
    xhr.open('post', 'getidf', true);
    var fd = new FormData();
    fd.append('request', 'showIdf');
    xhr.send(fd);
}

function updateAll() {
    console.log('Atualizar todos os dados armazenados da coleção');
    var xhr = new XMLHttpRequest();
    xhr.open('post', 'updateall', true);
    var fd = new FormData();
    fd.append('request', 'updateAll');
    xhr.send(fd);
}

function buscar() {
    var text = document.getElementById('inputBusca').value;
    console.log('Buscar: ', text);
    var xhr = new XMLHttpRequest();
    xhr.open('post', 'search', true);
    var fd = new FormData();
    fd.append('text', text);
    xhr.send(fd);
}