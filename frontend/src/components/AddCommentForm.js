import React, {Component} from "react";
import {
    MDBContainer,
    MDBIcon,
    MDBBtn,
} from 'mdbreact';
import './ItemDetailed.css'
import {addNewComment} from "../Api";
import {toast} from "react-toastify";

class AddCommentForm extends Component {
    state = {
        title: '',
        comment: ''
    };

    onSubmit = async (event) => {

        const body = {
            title: this.state.title,
            comment: this.state.comment,
            image: "",
            user_id: this.props.user_id,
            item_id: parseInt(this.props.item_id)
        };
        event.preventDefault();

        const resp = await addNewComment(body);
        if (resp) {
            toast.success(`Comment created`);
        }
    };

    onChangeTitle = (event) => {
        this.setState({title: event.target.value});
    };

    onChangeComment = (event) => {
        this.setState({comment: event.target.value});
    };

    render() {
        return (
            <MDBContainer>
                <form onSubmit={this.onSubmit}>
                    <p className="h5 py-1">Leave a comment</p>

                    <input type="text" name="name" id="defaultFormCardNameEx" className="form-control"
                           value={this.state.name}
                           onChange={this.onChangeTitle}
                    placeholder="Title"/>
                    <br/>
                    <textarea type="text" id="defaultFormContactMessageEx" className="form-control" rows="3"
                              value={this.state.description}
                              onChange={this.onChangeComment}
                    placeholder="Text for comment"/>
                    <div className="text-right py-2 mt-1">
                        <MDBBtn className="btn btn-outline-purple" type="submit">
                            Add!
                            <MDBIcon far icon="paper-plane" className="ml-2"/>
                        </MDBBtn>
                    </div>
                </form>
            </MDBContainer>
        )
    }
}

export default AddCommentForm;