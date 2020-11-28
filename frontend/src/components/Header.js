import React, {Component} from 'react';
import {MDBNavbar, MDBNavbarBrand, MDBNavbarNav, MDBNavbarToggler, MDBCollapse, MDBNavItem, MDBNavLink} from 'mdbreact';
import {Link} from 'react-router-dom';

class Header extends Component {
    state = {
        collapse: null,
    };

    render() {
        return (
            <header>
                <MDBNavbar style={{backgroundColor: "#FFFFFF"}} light expand="md" fixed="top" scrolling>
                    <Link to="/"><MDBNavbarBrand>Умный город IQ</MDBNavbarBrand></Link>
                    <MDBNavbarToggler/>
                    <MDBCollapse isOpen={this.state.collapse} navbar>
                        <MDBNavbarNav left>
                            <MDBNavItem>
                                <MDBNavLink to="/stats">Статистики</MDBNavLink>
                            </MDBNavItem>
                            <MDBNavItem>
                                <MDBNavLink to="/map">Регионы</MDBNavLink>
                            </MDBNavItem>
                            <MDBNavItem>
                                <MDBNavLink to="/datamap">Карта данных</MDBNavLink>
                            </MDBNavItem>
                            <MDBNavItem>
                                <MDBNavLink to="/addscript">Добавить парсер</MDBNavLink>
                            </MDBNavItem>
                        </MDBNavbarNav>
                    </MDBCollapse>
                </MDBNavbar>
            </header>
        );
    }
}

export default Header;