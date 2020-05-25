function render_table_content_row (original_url, short_url) {
    let table_row_content = document.createElement("tr");

    let original_url_element = document.createElement("td");
    let original_url_link = document.createElement("a");
    original_url_link.href = original_url;
    let original_url_text = document.createTextNode(original_url.slice(0, 35) + "...");
    original_url_link.appendChild(original_url_text);
    original_url_element.appendChild(original_url_link);

    let short_url_element = document.createElement("td");
    let short_url_link = document.createElement("a");
    short_url_link.href = short_url;
    let short_url_text = document.createTextNode(`http://localhost:8000/${short_url}`);
    short_url_link.appendChild(short_url_text);
    short_url_element.appendChild(short_url_link);

    table_row_content.appendChild(original_url_element);
    table_row_content.appendChild(short_url_element);

    document.getElementById("urls-table").appendChild(table_row_content);
}

let form = {
    original_url: document.getElementById('original_url'),
    short_url: document.getElementById('short_url'),
    submit: document.getElementById('submit')
};

function getCookie(name) {
    let cookieValue = null;
    if (document.cookie && document.cookie !== '') {
        var cookies = document.cookie.split(';');
        for (var i = 0; i < cookies.length; i++) {
            var cookie = cookies[i].trim();
            if (cookie.substring(0, name.length + 1) === (name + '=')) {
                cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                break;
            }
        }
    }
    return cookieValue;
}
let csrftoken = getCookie('csrftoken');

document.getElementById("submit").addEventListener('click', function (e) {
    e.preventDefault();
    let request = new XMLHttpRequest();

    request.onload = function () {
        let responseObj;
        responseObj = JSON.parse(request.responseText);
        if (responseObj.status === 'fail') {
            alert(responseObj.message);
        } else {
            let short_url = `http://localhost:8000/${responseObj['message']['short_url']}`;
            let link = document.createElement("a");
            link.href = short_url;
            let link_text = document.createTextNode(short_url);
            link.appendChild(link_text);

            let div = document.getElementById("short-url-holder");
            div.appendChild(link);

            render_table_content_row(responseObj.message['original_url'], responseObj.message['short_url']);
        }
    };

    let data = {
        original_url: form.original_url.value,
    };

    let expression = /[-a-zA-Z0-9@:%._\+~#=]{1,256}\.[a-zA-Z0-9()]{1,6}\b([-a-zA-Z0-9()@:%_\+.~#?&//=]*)?/gi;
    let regex = new RegExp(expression);
    if (data.original_url.match(regex)) {
         if (form.short_url.value !== '') {
        data.short_url = form.short_url.value
        }
        let json_data = JSON.stringify(data);

        request.open('post', '/api/short/');
        request.setRequestHeader('Content-Type', 'application/json');
        request.setRequestHeader('X-CSRFToken', csrftoken);
        request.send(json_data);
    }
    else {
        alert('Enter a valid URL Address');
        form.original_url.value = ''
    }
});