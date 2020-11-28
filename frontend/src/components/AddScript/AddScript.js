import React, {Component} from "react";
import {
    MDBContainer,
    MDBIcon,
    MDBBtn,
} from 'mdbreact';
import {addNewScript} from '../../Api'
import {toast} from "react-toastify";


class AddScript extends Component {
    state = {
        file: null,
        fileName: '',
    };

    onSubmit = async (event) => {
        event.preventDefault();
        if (!this.state.file)
            return;
        const formData = new FormData()
        formData.append('script', this.state.file)


        const resp = await addNewScript(formData);
        if (resp) {
            toast.success(`Скрипт добавлен`);
            this.props.history.push({
                pathname: '/stats',
            });
        }
    };

    reader;
    onFileRead = (e) => {
        const encodedImg = this.reader.result.split(',')[1];
        this.setState({encodedImg});
    };


    onChangeFile = (event) => {
        const file = event.target.files[0]
        const fileName = event.target.files[0].name
        this.setState({file, fileName});
    };


    render() {
        return (
            <MDBContainer className="w-75">
                <form onSubmit={this.onSubmit}>
                    <p className="h4 text-center py-4">Добавьте файл Python script парсера </p>
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
                            {this.state.fileName || 'Выберите файл'}
                        </label>
                    </div>
                    <div className="text-center py-4 mt-3">
                        <MDBBtn className="btn btn-outline-purple" type="submit">
                            Отправить!
                            <MDBIcon far icon="paper-plane" className="ml-2"/>
                        </MDBBtn>
                    </div>
                </form>
            </MDBContainer>
        )
    }
}

export default AddScript;