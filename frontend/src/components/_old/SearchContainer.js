/*

This container holds elements on Search page:
- Search bar
 */

import React, {Component} from "react";
import SearchBar from "./SearchBar";
import {Link} from "react-router-dom";


class SearchContainer extends Component {

    filterChanged = (filterValue, enterHit) => {
        if (enterHit) {
            this.props.history.push({
                pathname: "/items",
                search: '?filter=' + filterValue,
            });
        }
    };


    render() {
        return (
            <div>
                <SearchBar onSearchChange={this.filterChanged}/>
                <Link to="/items">Show all items</Link>
            </div>
        );
    }
}

export default SearchContainer;