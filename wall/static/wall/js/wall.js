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
                             "</h3>\r\n" +
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
    message_id = $(this).children("input[name=message_id]").val()
    console.log("deleting message id #" + message_id)
    csrf_token = $("input[name=csrfmiddlewaretoken]").first().val()
    response = $.post("/api/message/delete", data).done(function(response) {
        if(response.success) {
            $("#message_" + message_id).remove()
        }
    })
}


function on_comment_post() {
    event.preventDefault()
    data = $(this).serialize()
    csrf_token = $("input[name=csrfmiddlewaretoken]").first().val()
    response = $.post("/api/comment/post", data).done(function(response) {
        console.log(response)
        if(response.success) {
            console.log("Success!")
            new_message = "<div class=\"div_comment\" id=\"comment_" + response.comment.id + "\"">\r\n" +
                               "<h5>" +
                                   response.author.first_name + " " +
                                   response.author.last_name + " - " +
                                   response.comment.created_at +
                               "</h5>\r\n" +
                               "<div class=\"div_comment_text\">\r\n" +
                                   "<p>" + response.comment.text + "</p>\r\n" +
                                   "<form method=POST action=\"comment/delete\" class=\"comment_delete_form\">\r\n" +
                                       "<input type=\"hidden\" name=\"csrfmiddlewaretoken\" value=\"" + csrf_token + "\">\r\n" +
                                       "<input type=\"hidden\" name=\"comment_id\" value=\"" + response.comment.id + "\">\r\n" +
                                       "<input type=\"submit\" value=\"Delete\">\r\n" +
                                   "</form>\r\n" +
                               "</div>\r\n" +
                           "</div>\r\n"
            console.log(response.message.id)
            $("#comments_for_message_" + response.message.id).append(new_message)
        }
    })
}


function on_comment_delete() {
    event.preventDefault()
    data = $(this).serialize()
    comment_id = $(this).children("input[name=comment_id]").val()
    response = $.post("/api/comment/delete", data).done(function(response) {
        if(response.success) {
            $("#comment_" + comment_id).remove()
        }
    })
}
