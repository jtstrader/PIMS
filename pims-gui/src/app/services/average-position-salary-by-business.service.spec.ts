import { TestBed } from '@angular/core/testing';

import { AveragePositionSalaryByBusinessService } from './average-position-salary-by-business.service';

describe('AveragePositionSalaryByBusinessService', () => {
  let service: AveragePositionSalaryByBusinessService;

  beforeEach(() => {
    TestBed.configureTestingModule({});
    service = TestBed.inject(AveragePositionSalaryByBusinessService);
  });

  it('should be created', () => {
    expect(service).toBeTruthy();
  });
});
