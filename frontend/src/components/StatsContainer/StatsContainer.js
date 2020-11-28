import React, {Component} from "react";
import {getStats} from "../../Api";
import StatsTable from "../StatsTable";


class StatsContainer extends Component {
    /*
     */

    constructor(props) {
        super(props);
        this.state = {
            statsData: null,
            loading: true,
        }
    }

    updateData = async () => {
        this.setState({loading: true});
        await new Promise((resolve) => {
            setTimeout(resolve, 500);
        });
        const statsData = await getStats();
        this.setState({statsData, loading: false});
    };

    componentDidMount() {
        this.updateData();
    }

    render() {
        return (
            <div>
                {this.state.loading ?
                    (
                        <div>
                            <div className="spinner-border text-success" role="status">
                                <span className="sr-only">Loading...</span>
                            </div>
                            Loading...
                        </div>
                    ) :
                    (
                        <StatsTable data={this.state.statsData}/>
                    )
                }
            </div>
        );
    }
}

export default StatsContainer;