import React, {Component} from "react";
import {
    MDBContainer,
    MDBRow,
    MDBCol,
    MDBView,
    MDBCard,
    MDBTable,
    MDBTableBody,
    MDBCardBody,
    MDBCardTitle,
    MDBBadge,
    MDBCardText, MDBBtn,
} from 'mdbreact';
import './ItemDetailed.css'
import ProfileHover from "./ProfileHover";
import {getImageUrl} from "../Api";
import {withRouter} from 'react-router-dom';
import {toast} from "react-toastify";
import {deleteItem} from "../Api";

class ItemDetailed extends Component {

    deleteItem = async () => {
        const resp = await deleteItem(this.props.item.id);
        if (resp) {
            toast.success(`Item deleted`);
            this.props.history.push({
                pathname: '/items',
            });
        }
    };


    render() {
        if (!this.props.item)
            return (<span>Loading...</span>);
        return (
            <MDBCard>
                <MDBRow>
                    <MDBCol sm="4" className="d-flex">
                        <MDBView hover zoom rounded className="w-100">
                            <img src={getImageUrl(this.props.item.image_url)} className="img-fluid"
                                 alt="" style={{width: "100%"}}/>
                        </MDBView>
                    </MDBCol>
                    <MDBCol>
                        <MDBCardBody className="px-sm-0">
                            <MDBCardTitle style={{fontSize: "2em"}}>{this.props.item.name}</MDBCardTitle>
                            <MDBContainer className="mx-0 px-0">
                                <MDBTable responsiveMd borderless className="right-details">
                                    <MDBTableBody>
                                        <tr>
                                            <td className="field-name align-text-bottom">Belongs to</td>
                                            <td><ProfileHover user={this.props.item.owner}/></td>
                                        </tr>
                                        <tr>
                                            <td className="field-name">Located in</td>
                                            <td>{this.props.item.location}</td>
                                        </tr>
                                        <tr>
                                            <td className="field-name">Status</td>
                                            <td>{this.props.item.status === 'free' ?
                                                <MDBBadge color="success">Free</MDBBadge>
                                                : <MDBBadge color="danger">Occupied</MDBBadge>}</td>
                                        </tr>
                                    </MDBTableBody>
                                </MDBTable>
                            </MDBContainer>
                        </MDBCardBody>

                    </MDBCol>
                </MDBRow>
                <MDBRow>
                    <MDBCol>
                        {this.props.item && this.props.userInfo && this.props.item.owner &&
                        this.props.item.owner.id === this.props.userInfo.user_id &&
                        <div className="px-5">
                            <MDBBtn onClick={this.deleteItem} outline color="danger">
                                Delete
                            </MDBBtn>
                            <MDBBtn onClick={() => {
                                this.props.editItem(this.props.item);
                                this.props.history.push({
                                    pathname: `/items/${this.props.item.id}/edit`,
                                });
                            }} outline color="warning">
                                Edit
                            </MDBBtn>
                        </div>}
                    </MDBCol>
                </MDBRow>
                <MDBRow>
                    <MDBCol>
                        <MDBCardBody>
                            <MDBCardText>
                                {this.props.item.description}
                            </MDBCardText>
                        </MDBCardBody>

                    </MDBCol>
                </MDBRow>
            </MDBCard>

        );
    }
}

export default withRouter(ItemDetailed);