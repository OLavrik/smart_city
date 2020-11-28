import React, {Component} from "react";

import {withRouter} from 'react-router'
import ItemDetailed from "./ItemDetailed";
import CommentsList from "./CommentsList";
import {getItemDetails} from "../Api";
import {getComments} from "../Api";


class ItemDetailedContainer extends Component {
    state = {
        item: null,
        comments: null,
    };

    componentDidMount() {
        const id = this.props.match.params.id;
        this.fetchData(id);
    }

    fetchData = async (id) => {
        const item = await getItemDetails(id);
        const comments = await getComments(id);
        this.setState({item, comments});
    };


    render() {
        return (
            <div><ItemDetailed item={this.state.item} userInfo={this.props.userInfo} editItem={this.props.editItem}/>
                <CommentsList comments={this.state.comments} item_id={this.props.match.params.id}
                              user_id={this.props.userInfo && this.props.userInfo.user_id}/></div>
        );
    }
}

export default withRouter(ItemDetailedContainer);