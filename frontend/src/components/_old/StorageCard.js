import React, {Component} from "react";
import {
    MDBCard,
    MDBCardBody,
    MDBCardTitle,
} from "mdbreact";
import {Link} from 'react-router-dom';
import './StorageCard.css';

class StorageCard extends Component {

    render() {
        const storage = this.props.storage;
        return (
            <MDBCard className="d-flex flex-row flex-wrap my-3">
                    <MDBCardBody>
                        <MDBCardTitle><Link className="storage-card-title"
                                            to={`/storages/${this.props.storage.id}`}>{storage.name}</Link></MDBCardTitle>
                    </MDBCardBody>
            </MDBCard>
    );
    }
    }

    export default StorageCard;