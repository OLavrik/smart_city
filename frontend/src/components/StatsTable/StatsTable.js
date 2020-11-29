import React, {Component} from "react";
import {MDBContainer, MDBRow, MDBCol} from 'mdbreact';
import {MDBTable, MDBTableBody, MDBTableHead} from 'mdbreact';


class StatsTable extends Component {
    componentDidUpdate(prevProps, prevState, snapshot) {
    }

    componentDidMount() {

    }

    composeHead = data => {
        if (!data || !data.columns)
            return null;
        const headers =
            data.columns.map(function (el, i) {
                return <th key={i}>{el}</th>;
            });

        return (<MDBTableHead>
            <tr>
                {headers}
            </tr>
        </MDBTableHead>);
    }

    composeRow = (row) => {
        if (Array.isArray(row)) {
            return (
                <tr>
                    {row && row.map(function (el, i) {
                        return <td key={i}>{typeof el === "number" ? el.toFixed(2): el}</td>;
                    })}
                </tr>
            )
        }
        else
        {
            const arrOfRows = Object.values(row)[0];
            return arrOfRows.map(row => (
                <tr>
                    {row && row.map(function (el, i) {
                        return <td key={i}>{typeof el === "number" ? el.toFixed(2): el}</td>;
                    })}
                </tr>
            ))
        }
    }

    composeBody = data => {
        if (!data || !data.data)
            return null;

        const rows = data.data.map( row => this.composeRow(row));

        return (
            <MDBTableBody>
                {rows}
            </MDBTableBody>
        );
    }

    render() {
        const data = this.props.data;
        if (!data)
            return null;
        console.log("This is data", data);
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