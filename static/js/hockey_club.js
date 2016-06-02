var firstCall = true;
var lastComment;
var allComments;

function getTweets() {
    $.ajax({
        url: "{% url 'news:news_page' news.id %}",
        type: "GET",
        success: function (resp) {
            addCommentToPage(resp);
        }
    })
}

function addCommentToPage(comments) {
    var parent = $("#comments");
    allComments = comments;
    if (firstCall) {
        comments.forEach(function (item, i, arr) {
            //{#                    console.log(item);#
            //}
            parent.append("<div class='row'><div class='col-sm-1'>" +
                "<div class='thumbnail'>" +
                "<img class='img-responsive user-photo' src=" + item.fields.author.image.url + ">" +
                "</div></div><div class='col-sm-5'><div class='panel panel-default'><div class='panel-heading'>" +
                "<strong>" + item.fields.author.username + "</strong><span class='text-muted'>" +
                item.fields.publication_date + "</span></div><div class='panel-body'>" + item.fields.comment + "</div>" +
                "</div></div></div>")
        });
        firstCall = false;
        lastComment = comments[comments.length - 1];
    }
    else {
        if (lastComment !== undefined) {
            var newTweet = comments[comments.length - 1];
            console.log(newTweet);
            if (newTweet.pk !== lastComment.pk) {
                lastComment = newTweet;
                parent.append("<div class='row'><div class='col-sm-1'>" +
                "<div class='thumbnail'>" +
                "<img class='img-responsive user-photo' src=" + item.fields.author.image.url + ">" +
                "</div></div><div class='col-sm-5'><div class='panel panel-default'><div class='panel-heading'>" +
                "<strong>" + item.fields.author.username + "</strong><span class='text-muted'>" +
                item.fields.publication_date + "</span></div><div class='panel-body'>" + item.fields.comment + "</div>" +
                "</div></div></div>")
            }
        }
    }
}
$(document).ready(function () {
    setInterval(getTweets(), 1000);

    $('#add_comment').click(function () {
        $.ajax({
            url: "{% url 'news:news_page' news.id %}",
            type: "POST",
            data: {
                'csrfmiddlewaretoken': $.cookie().csrftoken,
                'text': $('comment').val()
            },
            success: function (resp) {
                addCommentToPage(resp)
            }
        });
    });
});