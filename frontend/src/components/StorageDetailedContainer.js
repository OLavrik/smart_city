import React, {Component} from "react";

import {withRouter} from 'react-router'
import StorageDetailed from "./StorageDetailed";
import {getStorageDetails} from "../Api";


class StorageDetailedContainer extends Component {
    state = {
        storage: null,
    };

    componentDidMount() {
        const id = this.props.match.params.id;
        this.fetchData(id);
    }

    fetchData = async (id) => {
        const storage = await getStorageDetails(id);
        this.setState({storage});
    };



    render() {
        return (
            <StorageDetailed storage={this.state.storage} userInfo={this.props.userInfo}/>
        );
    }
}

export default withRouter(StorageDetailedContainer);