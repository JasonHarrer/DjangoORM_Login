$(document).ready(function() {
    $(".message_post_form").submit(on_message_post)
    $(".message_delete_form").submit(on_message_delete)
    $(".comment_post_form").submit(on_comment_post)
    $(".comment_delete_form").submit(on_comment_delete)
})


function on_message_post() {
    event.preventDefault()
    data = $(this).serialize()
    csrf_token = $("input[name=csrfmiddlewaretoken]").first().val()
    response = $.post("/api/message/post", data).done(function(response) {
        if(response.success) {
            var new_message ="<h3>" +
                                response.author.first_name + " " +
                                response.author.last_name + " - " +
                                response.message.created_at +
                             "</h3>" +
                             "<div class=\"div_message_text\" id=\"message_" + response.message.id + "\">\r\n" +
                                 "<p>" + response.message.text + "</p>\r\n" +
                                 "<form method=POST action=\"message/delete\" class=\"message_delete_form\">\r\n" +
                                     "<input type=\"hidden\" name=\"csrfmiddlewaretoken\" value=\"" + csrf_token + "\">\r\n" +
                                     "<input type=\"hidden\" name=\"message_id\" value = \"" + response.message.id + "\">\r\n" +
                                     "<input type=\"submit\" value=\"Delete\">\r\n" +
                                 "</form>\r\n" +
                             "</div>\r\n" +
                             "<form method=POST action=\"comment/post\" class=\"comment_post_form\">\r\n" +
                                 "<input type=\"hidden\" name=\"csrfmiddlewaretoken\" value=\"" + csrf_token + "\">\r\n" +
                                "<input type=\"hidden\" name=\"message_id\" value=\"" + response.message.id + "\">\r\n" +
                                "<label for=\"comment_text\">Post a comment</label>\r\n" +
                                "<textarea id=\"comment_text\" name=\"comment_text\" required></textarea>\r\n" +
                                "<input type=\"submit\" id=\"comment_submit\" value=\"Post a comment\">\r\n" +
                            "</form>\r\n"
            $("#div_message_list").prepend(new_message)
        }
    })
}


function on_message_delete() {
    event.preventDefault()
    data = $(this).serialize()
    response = $.post("/api/message/delete", data)
    if(response.success) {
        $("#message_" + data.message_id).remove()
    }
    console.log(response)
}


function on_comment_post() {
    event.preventDefault()
    data = $(this).serialize()
    response = $.post("/api/comment/post", data)
    console.log(response)
}


function on_comment_delete() {
    event.preventDefault()
    data = $(this).serialize()
    response = $.post("/api/comment/delete", data)
    console.log(response)
}
