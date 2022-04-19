package com.pims.api.models;

import com.fasterxml.jackson.annotation.JsonBackReference;
import com.fasterxml.jackson.annotation.JsonIgnoreProperties;
import com.fasterxml.jackson.annotation.JsonManagedReference;

import javax.persistence.*;
import java.math.BigInteger;
import java.sql.Date;
import java.util.List;

@Entity(name="Business")
@JsonIgnoreProperties({"hibernateLazyInitializer", "handler","contacts"})
public class Business {
    @Id
    private Integer business_id;
    private String name;
    private BigInteger worth;
    private Integer founding_year;

    @OneToMany(mappedBy = "business")
    @JsonManagedReference
    private List<Occupation> occupations;

    @OneToOne(mappedBy = "business")
    @JsonManagedReference
    private BusinessLocation businessLocation;

    public Business(){}

    public Integer getBusiness_id() {
        return business_id;
    }

    public void setBusiness_id(Integer business_id) {
        this.business_id = business_id;
    }

    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }

    public BigInteger getWorth() {
        return worth;
    }

    public void setWorth(BigInteger worth) {
        this.worth = worth;
    }

    public Integer getFounding_year() {
        return founding_year;
    }

    public void setFounding_year(Integer founding_year) {
        this.founding_year = founding_year;
    }

    public List<Occupation> getOccupations() {
        return occupations;
    }

    public void setOccupations(List<Occupation> occupations) {
        this.occupations = occupations;
    }

    public BusinessLocation getBusinessLocation() {
        return businessLocation;
    }

    public void setBusinessLocation(BusinessLocation businessLocation) {
        this.businessLocation = businessLocation;
    }
}
