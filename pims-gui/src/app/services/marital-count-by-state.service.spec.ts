import { TestBed } from '@angular/core/testing';

import { MaritalCountByStateService } from './marital-count-by-state.service';

describe('MaritalCountByStateService', () => {
  let service: MaritalCountByStateService;

  beforeEach(() => {
    TestBed.configureTestingModule({});
    service = TestBed.inject(MaritalCountByStateService);
  });

  it('should be created', () => {
    expect(service).toBeTruthy();
  });
});
