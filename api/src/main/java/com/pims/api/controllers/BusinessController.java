package com.pims.api.controllers;

import com.pims.api.models.Business;
import com.pims.api.repositories.BusinessRepository;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.PathVariable;
import org.springframework.web.bind.annotation.RequestMapping;
import org.springframework.web.bind.annotation.RestController;

import java.util.List;
import java.util.Optional;

@RestController
@RequestMapping("/api/business")
public class BusinessController {
    @Autowired
    private BusinessRepository businessRepository;

    @GetMapping
    public List<Business> List() { return businessRepository.findAll(); }

    @RequestMapping("{business_id}")
    public Business get(@PathVariable Integer business_id) { return businessRepository.getById(business_id); }
}
