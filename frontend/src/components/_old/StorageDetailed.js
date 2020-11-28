import React, {Component} from "react";
import {
    MDBContainer,
    MDBRow,
    MDBCol,
    MDBCard,
    MDBTable,
    MDBTableBody,
    MDBCardBody,
    MDBCardTitle,
    MDBBtn,
} from 'mdbreact';
import './StorageDetailed.css'
import ProfileHover from "./ProfileHover";
import {withRouter} from 'react-router-dom';
import {toast} from "react-toastify";
import {deleteStorage} from "../Api";

class StorageDetailed extends Component {

    deleteStorage = async () => {
        const resp = await deleteStorage(this.props.storage.id);
        if (resp) {
            toast.success(`Storage deleted`);
            this.props.history.push({
                pathname: '/storages',
            });
        }
    };

    render() {
        if (!this.props.storage)
            return (<span>Loading...</span>);
        return (
            <MDBCard>
                <MDBRow>
                    <MDBCol>
                        <MDBCardBody className="px-sm-0">
                            <MDBCardTitle style={{fontSize: "2em"}}>{this.props.storage.name}</MDBCardTitle>
                            <MDBContainer className="mx-0 px-0">
                                <MDBTable responsiveMd borderless className="right-details">
                                    <MDBTableBody>
                                        <tr>
                                            <td className="field-name align-text-bottom">Belongs to</td>
                                            <td><ProfileHover user={this.props.storage.owner}/></td>
                                        </tr>
                                        <tr>
                                            <td className="field-name">Located in</td>
                                            <td>{this.props.storage.location}</td>
                                        </tr>
                                    </MDBTableBody>
                                </MDBTable>
                            </MDBContainer>
                        </MDBCardBody>

                    </MDBCol>
                </MDBRow>
                <MDBRow>
                    <MDBCol>
                        {this.props.storage && this.props.userInfo && this.props.storage.owner.id &&
                        this.props.storage.owner.id === this.props.userInfo.user_id &&
                        <div className="px-5">
                            <MDBBtn onClick={this.deleteStorage} outline color="danger">
                                Delete
                            </MDBBtn>
                        </div>}
                    </MDBCol>
                </MDBRow>
            </MDBCard>

        );
    }
}

export default withRouter(StorageDetailed);