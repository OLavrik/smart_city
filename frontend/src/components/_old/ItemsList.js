import React, {Component} from "react";
import ItemCard from "./ItemCard";
import Paginator from "./Paginator";

class ItemsContainer extends Component {
    static defaultProps = {
        pagination: true,
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
            perPage: props.perPage,
            offset: 0,
            loading: false,
        };
    }

    componentDidUpdate(prevProps, prevState) {
        if (this.useLoader) {
            if (prevProps.loader !== this.props.loader ||
                prevProps.pagination !== this.props.pagination ||
                prevState.offset !== this.state.offset ||
                prevState.perPage !== this.state.perPage) {

                if (prevProps.loader !== this.props.loader)
                    this.setState({offset: 0});
                this.updateData();
            }
        } else {
            if (prevProps.data !== this.props.data)
                this.setState({offset: 0});
        }
    }

    updateData = async () => {
        this.setState({loading: true});
        await new Promise((resolve) => {
            setTimeout(resolve, 500);
        });
        const limit = this.props.pagination ? this.state.perPage : null;
        const offset = this.props.pagination ? this.state.offset : 0;
        const data = await this.props.loader(offset, limit);
        this.setState({data, loading: false});
    };

    componentDidMount() {
        if (this.useLoader) {
            this.updateData();
        }
    }

    paginate = (page) => {
        const offset = (page - 1) * this.state.perPage;
        this.setState({offset});
    };


    render() {
        const active = 1 + this.state.offset / this.state.perPage;
        let itemsData, pagesCnt;
        if (this.useLoader) {
            itemsData = this.state.data || {items: [], totalCnt: 0};
            pagesCnt = Math.max(1, Math.ceil(itemsData.totalCnt / this.state.perPage));
        } else {
            const itemsArr = this.props.data || [];
            itemsData = {items: itemsArr, totalCnt: itemsArr.length};
            if (this.props.pagination) {
                itemsData.items = itemsData.items.slice(this.state.offset, this.state.offset + this.state.perPage);
                pagesCnt = Math.max(1, Math.ceil(itemsData.totalCnt / this.state.perPage));
            }
        }
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
                    ) : (
                        <div>
                            {itemsData.totalCnt ? itemsData.items.map((item, i) => {
                                return <ItemCard item={item} key={i}/>;
                            }) : (<span>Nothing to show</span>)}
                        </div>
                    )
                }
                {this.props.pagination &&
                <div className="d-flex justify-content-center">
                    <Paginator total={pagesCnt} paginate={this.paginate} active={active}/>
                </div>}
            </div>
        );
    }
}

export default ItemsContainer;