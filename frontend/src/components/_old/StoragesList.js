import React, {Component} from "react";
import StorageCard from "./StorageCard";

class StoragesContainer extends Component {
    static defaultProps = {
        pagination: false,
        perPage: 2
    };

    constructor(props) {
        super(props);
        if (props.loader && props.data) {
            throw new Error("Only one of 'loader' and 'data' props should be used")
        }
        this.useLoader = !!(props.loader);
        this.state = {
            data: null,
            loading: false,
        };
    }

    componentDidUpdate(prevProps, prevState) {
        if (this.useLoader) {
            if (prevProps.loader !== this.props.loader) {
                this.updateData();
            }
        }
    }

    updateData = async () => {
        this.setState({loading: true});
        await new Promise((resolve) => {
            setTimeout(resolve, 500);
        });
        const data = await this.props.loader();
        this.setState({data, loading: false});
    };

    componentDidMount() {
        if (this.useLoader) {
            this.updateData();
        }
    }


    render() {
        let storagesData;
        if (this.useLoader) {
            storagesData = this.state.data || {storages: [], totalCnt: 0};
        }
        return (
            <div>
                {this.state.loading ?
                    (
                        <div>
                            <div className="spinner-border text-success" role="status">
                                <span className="sr-only">Loading...</span>
                            </div>
                        </div>
                    ) : (
                        <div>
                            {storagesData ? storagesData.storages.map((storage, i) => {
                                return <StorageCard storage={storage} key={i}/>;
                            }) : (<span>Nothing to show</span>)}
                        </div>
                    )
                }
            </div>
        );
    }
}

export default StoragesContainer;