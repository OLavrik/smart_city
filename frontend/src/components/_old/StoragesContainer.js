/*

This container holds all elements on Storage page:
- Search bar
- List of storages
 */

import React, {Component} from "react";
import {getStorages} from "../Api";
import StoragesList from "./StoragesList";
import SearchBar from "./SearchBar";


class StoragesContainer extends Component {

    state = {
        owner_id: null,
    };

    owner_idChanged = (owner_id, enterHit) => {
        if (enterHit) {
            this.props.history.push({
                search: '?owner_id=' + owner_id,
            });
        } else {
            this.setState({owner_id: owner_id});
        }
    };

    getStoragesLoader(owner_id) {
        return async () => getStorages(owner_id);
    }

    componentDidMount() {
        const params = new URLSearchParams(this.props.location.search);
        this.setState({owner_id: params.get("owner_id")});
    }

    render() {
        return (
            <div>
                <SearchBar onSearchChange={this.owner_idChanged}/>
                <StoragesList loader={this.getStoragesLoader(this.state.owner_id)}/>
            </div>
        );
    }
}

export default StoragesContainer;