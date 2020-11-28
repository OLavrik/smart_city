import React, {Component} from "react";
import {
    MDBCard,
    MDBCardBody,
    MDBCardImage,
    MDBBtn,
    MDBCardTitle,
} from "mdbreact";
import {Link} from 'react-router-dom';
import TooltipTrigger from 'react-popper-tooltip';
import 'react-popper-tooltip/dist/styles.css';
import './ProfileHover.css'
import {getImageUrl} from "../Api";



class Tooltip extends Component {

    tooltip = ({tooltipRef, getTooltipProps}) => (
        <div
            {...getTooltipProps({
                ref: tooltipRef,
            })}
        >
            {this.props.tooltip}
        </div>);

    tooltipLink = ({getTriggerProps, triggerRef}) => (
        <span {...getTriggerProps({ref: triggerRef, className: 'trigger'})}>
            {this.props.children}
        </span>
    );


    render() {
        return (
            <TooltipTrigger {...this.props} tooltip={this.tooltip}>
                {this.tooltipLink}
            </TooltipTrigger>
        )
    }
}

class ProfileHover extends Component {


    render() {
        const user = this.props.user;
        return (
            <Tooltip placement="bottom" trigger="hover" hideArrow delayHide="200" tooltip={
                <MDBCard className="d-flex flex-row flex-wrap my-3">
                    <Link to={`/profile/${user.id}`}><MDBCardImage style={{height: "100px"}}
                                                                   className="img-fluid"
                                                                   src={getImageUrl(user.image_url)}
                                                                   alt=""/></Link>
                    <MDBCardBody>
                        <MDBCardTitle><Link className="profile-hover-card-title"
                                            to={`/profile/${user.id}`}>{user.username}</Link></MDBCardTitle>
                        <Link to={`/profile/${user.id}`}><MDBBtn outline color="success" size="sm">Contact!</MDBBtn></Link>
                    </MDBCardBody>
                </MDBCard>}>
                <span>{user.username}</span>
            </Tooltip>
        );
    }
}

export default ProfileHover;