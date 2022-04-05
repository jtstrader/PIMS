package com.pims.api.models;

import com.fasterxml.jackson.annotation.JsonIgnoreProperties;

import javax.persistence.*;
import java.math.BigInteger;
import java.sql.Date;
import java.util.List;

@Entity(name="Business")
@JsonIgnoreProperties({"hibernateLazyInitializer", "handler"})
public class Business {
    @Id
    private Integer business_id;
    private String name;
    private BigInteger worth;
    private Date founding_year;

    @OneToMany(mappedBy = "business")
    private List<Occupation> occupations;

    @OneToOne
    @JoinColumn(name="business_id")
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

    public Date getFounding_year() {
        return founding_year;
    }

    public void setFounding_year(Date founding_year) {
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
