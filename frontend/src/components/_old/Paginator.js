import React, {Component} from "react";
import {MDBPagination, MDBPageItem, MDBPageNav} from 'mdbreact';

class Paginator extends Component {

    render() {
        const items = [];
        for (let number = 1; number <= this.props.total; number++) {
            items.push(
                <MDBPageItem onClick={() => {
                    this.props.paginate(number);
                    this.setState({active: number})
                }} key={number} active={number === this.props.active}>
                    <MDBPageNav>{number}</MDBPageNav>
                </MDBPageItem>,
            );
        }

        return (
            <div>
                <MDBPagination size="lg">{items}</MDBPagination>
                <br/>
            </div>
        );
    }
}

export default Paginator;