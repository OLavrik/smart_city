import React, {Component} from "react";
import {
    MDBCard
} from 'mdbreact';
import {withRouter} from 'react-router-dom';
import CommentCard from "./CommentCard";
import AddCommentForm from "./AddCommentForm";

class CommentsList extends Component {

    render() {
        const comments = this.props.comments;
        if (!comments)
            return (<span>Loading...</span>);
        return (
            <div>
                    <h3 className="text-center my-2">Comments</h3>
                    {comments.count ? comments.comments.map((comment, i) => {
                        return <CommentCard comment={comment} key={i} user_id = {this.props.user_id}/>;
                    }) : (<span>No comments yet</span>)}

                <MDBCard>
                    <AddCommentForm item_id = {this.props.item_id} user_id = {this.props.user_id}/>
                </MDBCard>
            </div>
        );
    }
}
export default withRouter(CommentsList);