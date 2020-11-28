import React, {Component} from "react";
import {MDBContainer, MDBRow, MDBCol} from 'mdbreact';
import {MDBTable, MDBTableBody, MDBTableHead} from 'mdbreact';


class StatsTable extends Component {
    componentDidUpdate(prevProps, prevState, snapshot) {
    }

    componentDidMount() {

    }

    composeHead = data => {
        if (!data || !data.headers)
            return;
        const headers =
            data.headers.map(function (el, i) {
                return <th key={i}>{el}</th>;
            });

        return (<MDBTableHead>
            <tr>
                <th></th>
                {headers}
            </tr>
        </MDBTableHead>);
    }

    composeRow = (rowName, rowData) => {
        console.log(rowName);
        console.log(rowData);
        return (
            <tr>
                <td>{rowName}</td>
                {rowData && rowData.map(function (el, i) {
                    return <td key={i}>{el}</td>;
                })}
            </tr>
        )
    }

    composeBody = data => {
        if (!data || !data.data)
            return;

        const rows = Object.entries(data.data).map( arr => this.composeRow(...arr));

        return (
            <MDBTableBody>
                {rows}
            </MDBTableBody>
        );
    }

    render() {
        const data = this.props.data;
        if (!data)
            return;
        console.log(data);
        const tableHead = this.composeHead(data);
        const tableBody = this.composeBody(data);
        return (
            <MDBContainer>
                <MDBTable hover small bordered>
                    {tableHead}
                    {tableBody}
                </MDBTable>
            </MDBContainer>
        );
    }
}

export default StatsTable;