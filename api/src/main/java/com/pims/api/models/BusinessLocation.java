package com.pims.api.models;

import com.fasterxml.jackson.annotation.JsonBackReference;
import com.fasterxml.jackson.annotation.JsonIgnore;
import com.fasterxml.jackson.annotation.JsonIgnoreProperties;
import com.fasterxml.jackson.annotation.JsonManagedReference;

import javax.persistence.*;
import java.math.BigInteger;
import java.sql.Date;
import java.util.List;

@Entity(name="business_location")
@JsonIgnoreProperties({"hibernateLazyInitializer", "handler"})
public class BusinessLocation {
    @Id
    private Integer business_id;
    private String address;
    private String city;
    private String state;
    private Integer zip;

    @OneToOne
    @PrimaryKeyJoinColumn
    @JsonBackReference
    private Business business;

    public BusinessLocation(){}

    public Integer getBusiness_id() {
        return business.getBusiness_id();
    }

    public void setBusiness_id(Integer business_id) {
        this.business.setBusiness_id(business_id);
    }

    public String getAddress() {
        return address;
    }

    public void setAddress(String address) {
        this.address = address;
    }

    public String getCity() {
        return city;
    }

    public void setCity(String city) {
        this.city = city;
    }

    public String getState() {
        return state;
    }

    public void setState(String state) {
        this.state = state;
    }

    public Integer getZip() {
        return zip;
    }

    public void setZip(Integer zip) {
        this.zip = zip;
    }

    public Business getBusiness() {
        return business;
    }

    public void setBusiness(Business business) {
        this.business = business;
    }
}
