import React, {Component} from "react";
import {
    MDBContainer,
    MDBIcon,
    MDBBtn,
} from 'mdbreact';
import './ItemDetailed.css'
import {addNewItem} from "../Api";
import {toast} from "react-toastify";


class AddItemForm extends Component {
    state = {
        name: '',
        description: '',
        file: '',
        encodedImg:'',
    };

     onSubmit = async (event) => {

        const body = {
            name: this.state.name,
            description: this.state.description,
            image: this.state.encodedImg
        };
        event.preventDefault();

        const resp = await addNewItem(body);
         if (resp) {
             toast.success(`Item created`);
             this.props.history.push({
                 pathname: '/items/' + resp.id,
             });
         }
    };

    onChangeName = (event) => {
        this.setState({name: event.target.value});
    };
    reader;
    onFileRead = (e) => {
        const encodedImg = this.reader.result.split(',')[1];
        this.setState({encodedImg});
    };


    onChangeFile = (event) => {
        this.reader = new FileReader();
        this.reader.onloadend = this.onFileRead;
        this.reader.readAsDataURL(event.target.files[0]);
        this.setState({file: event.target.files[0].name});
    };

    onChangeDescription = (event) => {
        this.setState({description: event.target.value});
    };

    render() {

        return (
            <MDBContainer className="w-75">
                <form onSubmit={this.onSubmit}>
                    <p className="h4 text-center py-4">Provide new item info</p>
                    <label htmlFor="defaultFormCardNameEx" className="grey-text font-weight-light">
                        Name
                    </label>
                    <input type="text" name="name" id="defaultFormCardNameEx" className="form-control"
                           value={this.state.name}
                           onChange={this.onChangeName}/>
                    <br/>

                    <div className="custom-file">
                        <input
                            type="file"
                            className="custom-file-input"
                            id="inputGroupFile01"
                            aria-describedby="inputGroupFileAddon01"
                            ref={input => {
                                this.fileInput = input;
                            }}
                            onChange={this.onChangeFile}
                        />
                        <label className="custom-file-label" htmlFor="inputGroupFile01">
                            {this.state.file || 'Choose file'}
                        </label>
                    </div>
                    <label htmlFor="defaultFormContactMessageEx" className="grey-text">
                        Description
                    </label>
                    <textarea type="text" id="defaultFormContactMessageEx" className="form-control" rows="3"
                              value={this.state.description}
                              onChange={this.onChangeDescription}/>
                    <div className="text-center py-4 mt-3">
                        <MDBBtn className="btn btn-outline-purple" type="submit">
                            Add!
                            <MDBIcon far icon="paper-plane" className="ml-2"/>
                        </MDBBtn>
                    </div>
                </form>
            </MDBContainer>
        )
    }
}

export default AddItemForm;