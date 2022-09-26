function upvote_downvote_fun(this_btn, post_id) {
  $.ajax({
    data: {
      post_id: post_id,
      vote_type: this_btn.title,
    },
    url: '/like/',
    type: 'GET',
    success: function (response) {
      document.getElementById('post_' + post_id).innerHTML =
        response.total_votes;
      if (response.upvote) {
        document.getElementById('upvote_' + post_id).style.color = 'blue';
        document.getElementById('downvote_' + post_id).style.color = 'black';
      } else if (response.downvote) {
        document.getElementById('upvote_' + post_id).style.color = 'black';
        document.getElementById('downvote_' + post_id).style.color = 'red';
      } else {
        document.getElementById('upvote_' + post_id).style.color = 'black';
        document.getElementById('downvote_' + post_id).style.color = 'black';
      }
    },
  });
}

function comment_fun(this_btn, post_id) {
  var cmnt_body = document.getElementById('cmnt_' + post_id + '_body').value;
  if (cmnt_body.length > 0) {
    $.ajax({
      data: {
        post_id: post_id,
        cmnt_body: cmnt_body,
      },
      url: '/comment/',
      type: 'GET',
      success: function (response) {
        if (this_btn.value == 'post_comment') {
          location.reload();
          return;
        } else if (this_btn.value == 'post') {
          document.getElementById('cmnt_' + post_id + '_body').value = null;
          document.getElementById('cmnt_username_' + post_id).innerHTML =
            response.cmnt_username + ' - ' + response.cmnt_date_added;
          document.getElementById('cmnt_body_' + post_id).innerHTML =
            response.cmnt_body;
        }
      },
    });
  }
}
