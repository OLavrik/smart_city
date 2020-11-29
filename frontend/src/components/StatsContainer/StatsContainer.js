import React, {Component} from "react";
import {getStatsList, getStatsByTag, getPDF} from "../../Api";
import StatsTable from "../StatsTable";
import {MDBDropdown, MDBDropdownToggle, MDBDropdownMenu, MDBDropdownItem, MDBContainer, MDBBtn} from "mdbreact";
import MapContainer from "../MapContainer";

class StatsContainer extends Component {
    /*
     */

    constructor(props) {
        super(props);
        this.state = {
            statsData: null,
            loading: false,
            selectedStat: null,
            statsList: null
        }
    }

    doGetStatsList = async () => {
        this.setState({loading: true});
        const statsList = await getStatsList();
        this.setState({statsList: statsList.statsTags, loading: false});
    };

    doGetStatsTable = async () => {
        this.setState({loading: true});
        const statsData = await getStatsByTag(this.state.selectedStat);
        this.setState({statsData: statsData.stats, loading: false});
    };

    onDropDownClickHandler = (event) => {
        const statsTag = event.target.value
        console.log("Selected stats", statsTag);
        this.setState({selectedStat: statsTag});
    };

    componentDidMount() {
        this.doGetStatsList();
    }

    componentDidUpdate(prevProps, prevState) {
        if (prevState.selectedStat !== this.state.selectedStat) {
            this.doGetStatsTable()
        }
    }
    onDownloadBtnCLick = () => {
        getPDF(this.state.selectedStat)
    }


    render() {
        console.log(this.state)
        const statsList = this.state.statsList && this.state.statsList.map(el => (
            <MDBDropdownItem onClick={this.onDropDownClickHandler} value={el.tag}
                             key={el.tag}>{el.title}</MDBDropdownItem>));
        return (
            <div>
                <div className="d-flex justify-content-center mb-4">
                    <MDBDropdown>
                        <MDBDropdownToggle caret color="info">
                            Статистики
                        </MDBDropdownToggle>
                        <MDBDropdownMenu basic>
                            {statsList ? statsList : <MDBDropdownItem disabled>loading...</MDBDropdownItem>}
                        </MDBDropdownMenu>
                    </MDBDropdown>
                </div>

                {this.state.loading ?
                    (
                        <div>
                            <div className="spinner-border text-success" role="status">
                                <span className="sr-only">Loading...</span>
                            </div>
                            Loading...
                        </div>
                    ) :
                    (this.state.statsData &&
                        <div>
                            <div className="d-flex justify-content-center">
                                <h3>{this.state.statsData.title}</h3>
                            </div>
                            <div>
                                <MapContainer data={this.state.statsData}/>
                            </div>
                            <div className="d-flex justify-content-center">
                                <MDBBtn onClick={this.onDownloadBtnCLick} className="mb-5">Скачать отчет</MDBBtn>
                            </div>
                            <StatsTable data={this.state.statsData}/>
                        </div>
                    )
                }
            </div>
        );
    }
}

export default StatsContainer;