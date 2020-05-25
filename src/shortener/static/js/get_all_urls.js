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

function render_table_heading_row () {
    let table_row_heading = document.createElement("tr");
    let original_heading = document.createElement("th");
    let original_heading_text = document.createTextNode("Original URL");
    original_heading.appendChild(original_heading_text);

    let short_heading = document.createElement("th");
    let short_heading_text = document.createTextNode("Short URL");
    short_heading.appendChild(short_heading_text);

    table_row_heading.appendChild(original_heading);
    table_row_heading.appendChild(short_heading);

    return table_row_heading;
}

window.onload = function () {
    let request = new XMLHttpRequest();

    request.onload = function () {
        let responseObj;
        responseObj = JSON.parse(request.responseText);
        let urls = responseObj['message'];

        if (responseObj.status !== 'fail') {
            let table_row_heading = render_table_heading_row();
            document.getElementById("urls-table").appendChild(table_row_heading);
        }

        urls.forEach(function (item) {
            render_table_content_row(item['original_url'], item['short_url']);
        })
    };

    request.open('get', '/api/short/');
    request.send();
};