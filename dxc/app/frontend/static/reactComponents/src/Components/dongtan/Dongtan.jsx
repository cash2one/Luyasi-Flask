import React from 'react';
import ReactDOM from 'react-dom';
import $ from 'jquery';
import './Dongtan.scss';

class DongtanInput extends React.Component{

    constructor(){
        super();
        //this.onChange = this.onChange.bind(this);
        this.state = {
            content: null,
            category_id: 7,
            title: '动弹'
        };
        this.handleChange = this.handleChange.bind(this);
        this.postDongtan = this.postDongtan.bind(this);
    }

    handleChange(e){
        this.setState({content: e.target.value.trim()});
    }

    postDongtan(e){
        e.preventDefault();

        if(!this.state.content || this.state.content===''){
            alert('请先输入内容');
            return;
        }

        $.ajax({
          headers: {'Appid': this.props.appid || ''},
          type: 'POST',
          url: this.props.url + '/blog-new',
          data: JSON.stringify(this.state),
          contentType:'application/json;charset=utf-8',
          success: function(data){
            alert('动弹成功');
            this.setState({content: ''});
          }.bind(this),

          error: function(xhr, status, err){
            if(xhr.status===401){
                alert('要先登录啦~');
            }else{
                alert('出错了~');
            }
          },
          dataType: 'json'
        });
        // $.get(this.props.url);
    }

    // handleChange = (e) => {
    //     this.setState({content: e.target.value});
    // }

    render(){
        return (
            <form noValidate onSubmit={this.postDongtan} className="dongtan-input">
                <div className="input-group">
                    <input required type="text" className="form-control" placeholder="今天你动弹了没？" value={this.state.content} onChange={this.handleChange}/>
                    <div className="input-group-btn">
                        <button type="submit" className="btn btn-success">动弹</button>
                    </div>
                </div>
            </form>
        );
    }
}


class DongtanItem extends React.Component{
    render(){
        return (
            <div className="dongtan-item">
                <div className="item-avatar"><img width="32" src={this.props.useravatar || '/static/images/avatar_default_72px.png'} className="img-responsive" alt="头像" /></div>
                <div className="item-content">{this.props.username}:<a href={this.props.blogUrlPrefix + '/' +this.props.itemId}> {this.props.content}</a></div>
            </div>
        );
    }
}

class DongtanList extends React.Component{
    render() {
        let dongtans = this.props.datas.map((dongtan) => {
            return <DongtanItem username={dongtan.username} userinfo={dongtan.userid} blogUrlPrefix={this.props.blogUrlPrefix}
                    useravatar={dongtan.useravatar} itemId={dongtan.id} key={dongtan.id} content={dongtan.content} />
        });

        return <div>{dongtans}</div>
    }
}

class Dongtan extends React.Component{
    constructor(){
        super();
        this.state = {
            dongtans:[]
        };
        this.loadDongtans = this.loadDongtans.bind(this);

    }

    loadDongtans(){
        $.ajax({
            headers: {'Appid': this.props.appid || ''},
            url: this.props.url + ';category=7;showcontent=True',
            dataType: 'json',
            type: 'GET',
            success: function(res){
                if(res.meta.success){
                    this.setState({dongtans: res.response.datas})
                }
            }.bind(this),
            error: function(xhr, status, err){
                console.error('加载动弹出错');
            }
        });
    }

    componentDidMount(){
        this.loadDongtans();
        setInterval(this.loadDongtans, 10000);
    }

    render(){
       
        return (
            <div>
                <DongtanInput url={this.props.url} appid={this.props.appid}/>
                <DongtanList datas={this.state.dongtans} blogUrlPrefix={this.props.blogUrlPrefix}/>
            </div>
        );
    }
}

ReactDOM.render(
    <Dongtan url="/blogs" appid="app0001" blogUrlPrefix='/blogs/blog/7'/>,
    document.getElementById('dongtan')
);

export default Dongtan;

